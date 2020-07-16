"""
azure-storage-blob Note

pipenv install azure-storage-blob

Document: https://docs.microsoft.com/ja-jp/azure/storage/blobs/storage-quickstart-blobs-python
"""


from azure.storage.blob import BlobServiceClient


# BlobServiceClient を作成します。
blob_service_client = BlobServiceClient.from_connection_string(
    CONNECTION_STRING)

# ContainerClient を作成します。
container_client = blob_service_client.get_container_client(
    CONTAINER_NAME)

# BlobClient を作成します。
blob_client = container_client.get_blob_client('100x100-dog.png')

# BlobClient は BlobServiceClient から直接、 ContainerClient をすっ飛ばして作ることも可能。
# blob_client = blob_service_client.get_blob_client(
#     container=CONTAINER_NAME, blob='100x100-dog.png')

# 画像を DL します。
downloaded_bytes = blob_client.download_blob().readall()
