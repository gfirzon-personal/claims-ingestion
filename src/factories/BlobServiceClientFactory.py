from azure.storage.blob import BlobServiceClient

from utils import config

class BlobServiceClientFactory:
    def __init__(self):
        config_dict = config.load_env_as_dict('.env')
        self.connection_string = config_dict['STORAGE_ACCOUNT_CONNECTIONSTRING']

    def create(self) -> BlobServiceClient:
        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        return blob_service_client
    