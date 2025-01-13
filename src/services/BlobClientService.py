from factories.BlobServiceClientFactory import BlobServiceClientFactory

class BlobClientService:
    """
    Class to read and write data to a blob file
    """
    #--------------------------------------------------------------------------------
    def __init__(self, container_name: str, blob_name: str):
        print("Initializing BlobClientService")
        self.blob_service_client = BlobServiceClientFactory().create()
        # Get the container client
        self.container_client = self.blob_service_client.get_container_client(container_name)
        # Get the blob client
        self.blob_client = self.container_client.get_blob_client(blob_name)        

    #--------------------------------------------------------------------------------
    def read_blob_file(self):   
        # Download the blob content
        blob_data = self.blob_client.download_blob().readall()        
        return blob_data.decode('utf-8')    

    #--------------------------------------------------------------------------------
    def append_block(self, block: str, header_line: str):

        # Create the blob if it doesn't exist
        if not self.blob_client.exists():
            self.blob_client.create_append_blob()
            self.blob_client.append_block(header_line)         

        # Append data to the blob       
        self.blob_client.append_block(block)         