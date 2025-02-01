from factories.BlobServiceClientFactory import BlobServiceClientFactory

class StorageService:
    def __init__(self):
        print("Initializing StorageService")
        self.blob_service_client = BlobServiceClientFactory().create()

    def set_container(self, container_name: str):
        self.container_name = container_name
        self.container_client = self.blob_service_client.get_container_client(container_name)

    def list_container_names(self):
        container_names = []
        containers = self.blob_service_client.list_containers()
        for container in containers:
            container_names.append(container['name'])
        return container_names   

    def list_files_in_container(self, container_name):
        file_names = []
        container_client = self.blob_service_client.get_container_client(container_name)
        blobs = container_client.list_blobs()
        for blob in blobs:
            file_names.append(blob.name)
        return file_names     

    def stream_blob_file(self, container_name, blob_name):    
        print(f"Streaming blob file: {blob_name} from container: {container_name}")
        # Get the container client
        container_client = self.blob_service_client.get_container_client(container_name)   
        # Get the blob client
        blob_client = container_client.get_blob_client(blob_name) 
        stream = blob_client.download_blob()
        return stream.chunks()      
    
    def stream_blob_file2(self, container_name, blob_name):
        print(f"Streaming blob file: {blob_name} from container: {container_name}")
        # Get the container client
        container_client = self.blob_service_client.get_container_client(container_name)   
        # Get the blob client
        blob_client = container_client.get_blob_client(blob_name) 
        stream = blob_client.download_blob()
        for chunk in stream.chunks(): 
            yield chunk
      