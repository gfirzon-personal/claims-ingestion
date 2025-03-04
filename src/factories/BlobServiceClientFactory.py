import logging
from azure.storage.blob import BlobServiceClient

from utils import config

config_dict = config.load_all_env_as_dict()

# Azurite emulator connection string
AZURITE_CONNECTION_STRING = (
    f"AccountKey={config_dict['AZURITE_ACCOUNT_KEY']};"
    f"AccountName={config_dict['AZURITE_ACCOUNT_NAME']};"
    f"BlobEndpoint={config_dict['AZURITE_BLOB_ENDPOINT']};"
)

use_azurite = config_dict['USE_AZURITE'].lower() == 'true'

class BlobServiceClientFactory:
    """Factory class to create a BlobServiceClient object"""
    def __init__(self):
        #logging.info(f"Initializing BlobServiceClientFactory using azurite={use_azurite}")

        if use_azurite:
            # Use Azurite settings
            logging.info(f"Using azurite as blob storage")
            self.connection_string = AZURITE_CONNECTION_STRING
        else:
            # Use Azure storage settings
            logging.info(f"Using Azure as blob storage")
            self.connection_string = config_dict['STORAGE_ACCOUNT_CONNECTIONSTRING']

    def create(self) -> BlobServiceClient:
        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)

        return blob_service_client
    