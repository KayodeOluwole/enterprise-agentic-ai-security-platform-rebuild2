
from pydantic import BaseModel


class ToolRequest(BaseModel):
    tool_name: str


class AuthorizationResult(BaseModel):
    tool_name: str
    role: str
    authorized: bool
    reason: str
