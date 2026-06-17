import base64
import json
from typing import List
from fastapi import Request


def get_client_principal(request: Request) -> dict:
    encoded_principal = request.headers.get("X-MS-CLIENT-PRINCIPAL")

    if not encoded_principal:
        return {}

    decoded_bytes = base64.b64decode(encoded_principal)
    decoded_json = decoded_bytes.decode("utf-8")

    return json.loads(decoded_json)


def get_user_roles(request: Request) -> List[str]:
    principal = get_client_principal(request)

    claims = principal.get("claims", [])

    roles = []

    for claim in claims:
        claim_type = claim.get("typ")
        claim_value = claim.get("val")

        if claim_type in [
            "roles",
            "http://schemas.microsoft.com/ws/2008/06/identity/claims/role"
        ]:
            roles.append(claim_value)

    return roles


def has_required_role(user_roles: List[str], required_role: str) -> bool:
    return required_role in user_roles
