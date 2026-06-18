from fastapi import FastAPI, Request, HTTPException

from app.models import ToolRequest
from app.registry import load_tool_registry
from app.auth import get_user_roles, has_required_role
from app.audit import write_audit_event


app = FastAPI(
    title="Enterprise MCP Authorization Server",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "enterprise-mcp-authorization-server"
    }


@app.get("/tools")
def list_tools():
    registry = load_tool_registry()

    enabled_tools = [
        {
            "name": tool["name"],
            "risk": tool["risk"],
            "enabled": tool["enabled"]
        }
        for tool in registry["tools"]
        if tool["enabled"] is True
    ]

    return {
        "tools": enabled_tools
    }


@app.post("/authorize-tool")
def authorize_tool(request_body: ToolRequest, request: Request):
    registry = load_tool_registry()
    user_roles = get_user_roles(request)

    requested_tool = None

    for tool in registry["tools"]:
        if tool["name"] == request_body.tool_name:
            requested_tool = tool
            break

    if requested_tool is None:
        audit = write_audit_event(
            event_type="MCP_TOOL_AUTHORIZATION",
            tool_name=request_body.tool_name,
            role="unknown",
            authorized=False,
            reason="Tool not found in registry"
        )

        raise HTTPException(
            status_code=404,
            detail=audit
        )

    required_role = requested_tool["requiredRole"]

    for role in user_roles:
        if has_required_role(user_roles, required_role):
            audit = write_audit_event(
                event_type="MCP_TOOL_AUTHORIZATION",
                tool_name=request_body.tool_name,
                role=role,
                authorized=True,
                reason="Required role matched"
            )
    if requested_tool.get("approvalRequired", False):
        audit = write_audit_event(
            event_type="MCP_TOOL_APPROVAL_REQUIRED",
            tool_name=request_body.tool_name,
            role=",".join(user_roles) if user_roles else "none",
            authorized=False,
            reason="Approval required before execution"
        )

        raise HTTPException(
            status_code=202,
            detail=audit
        )
            return audit

    audit = write_audit_event(
        event_type="MCP_TOOL_AUTHORIZATION",
        tool_name=request_body.tool_name,
        role=",".join(user_roles) if user_roles else "none",
        authorized=False,
        reason=f"Missing required role: {required_role}"
    )

    raise HTTPException(
        status_code=403,
        detail=audit
    )
