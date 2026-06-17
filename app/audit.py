import logging
from datetime import datetime, timezone


logger = logging.getLogger("mcp-audit")
logger.setLevel(logging.INFO)


def write_audit_event(
    event_type: str,
    tool_name: str,
    role: str,
    authorized: bool,
    reason: str
):
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "tool_name": tool_name,
        "role": role,
        "authorized": authorized,
        "reason": reason
    }

    logger.info(event)
    return event
