import os
import requests
import jwt
from jwt.algorithms import RSAAlgorithm
from fastapi import Request, HTTPException


TENANT_ID = os.getenv("TENANT_ID")
API_AUDIENCE = os.getenv("API_AUDIENCE")


def get_bearer_token(request: Request) -> str:
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return ""

    if not auth_header.lower().startswith("bearer "):
        return ""

    return auth_header.split(" ", 1)[1]


def get_signing_key(token: str):
    if not TENANT_ID:
        raise HTTPException(status_code=500, detail="TENANT_ID not configured")

    jwks_url = f"https://login.microsoftonline.com/{TENANT_ID}/discovery/v2.0/keys"
    jwks = requests.get(jwks_url, timeout=10).json()

    unverified_header = jwt.get_unverified_header(token)
    kid = unverified_header.get("kid")

    for key in jwks["keys"]:
        if key["kid"] == kid:
            return RSAAlgorithm.from_jwk(key)

    raise HTTPException(status_code=401, detail="Signing key not found")


def validate_jwt(token: str) -> dict:
    signing_key = get_signing_key(token)

    issuer = f"https://login.microsoftonline.com/{TENANT_ID}/v2.0"

    return jwt.decode(
        token,
        signing_key,
        algorithms=["RS256"],
        audience=API_AUDIENCE,
        issuer=issuer
    )


def get_user_roles(request: Request):
    token = get_bearer_token(request)

    if not token:
        return []

    claims = validate_jwt(token)

    return claims.get("roles", [])


def has_required_role(user_roles, required_role):
    return required_role in user_roles
