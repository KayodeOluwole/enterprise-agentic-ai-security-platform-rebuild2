from typing import List, Optional
from fastapi import Request


def get_user_roles(request: Request) -> List[str]:
    roles_header = request.headers.get("X-MS-CLIENT-PRINCIPAL")

    if not roles_header:
        return []

    # App Service Easy Auth injects identity headers.
    # In Phase 2, we will expand this into full JWT/audit inspection.
    return []


def has_required_role(user_roles: List[str], required_role: str) -> bool:
    return required_role in user_roles
