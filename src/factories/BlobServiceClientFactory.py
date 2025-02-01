from azure.storage.blob import BlobServiceClient

from utils import config

config_dict = config.load_all_env_as_dict()

# Azurite emulator connection string
AZURITE_CONNECTION_STRING = (
    f"AccountKey={config_dict['AZURITE_ACCOUNT_KEY']};"
    f"AccountName={config_dict['AZURITE_ACCOUNT_NAME']};"
    f"BlobEndpoint={config_dict['AZURITE_BLOB_ENDPOINT']};"
)

class BlobServiceClientFactory:
    def __init__(self):
        self.connection_string = config_dict['STORAGE_ACCOUNT_CONNECTIONSTRING']

    def create(self) -> BlobServiceClient:
        # Create the BlobServiceClient object
        #blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        blob_service_client = BlobServiceClient.from_connection_string(AZURITE_CONNECTION_STRING)

        return blob_service_client
    