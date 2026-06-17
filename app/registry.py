import json
import os

from azure.identity import ManagedIdentityCredential
from azure.storage.blob import BlobServiceClient


def load_tool_registry():

    account_name = os.getenv("TOOL_REGISTRY_STORAGE_ACCOUNT")
    container_name = os.getenv("TOOL_REGISTRY_CONTAINER")
    file_name = os.getenv("TOOL_REGISTRY_FILE")

    credential = ManagedIdentityCredential()

    account_url = f"https://{account_name}.blob.core.windows.net"

    blob_service = BlobServiceClient(
        account_url=account_url,
        credential=credential
    )

    blob_client = blob_service.get_blob_client(
        container=container_name,
        blob=file_name
    )

    data = blob_client.download_blob().readall()

    return json.loads(data)
