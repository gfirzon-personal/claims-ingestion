from factories.BlobServiceClientFactory import BlobServiceClientFactory

class StorageService:
    def __init__(self):
        print("Initializing StorageService")
        self.blob_service_client = BlobServiceClientFactory().create()

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

    def read_blob_file(self, container_name, blob_name):
        # Get the container client
        container_client = self.blob_service_client.get_container_client(container_name)
        
        # Get the blob client
        blob_client = container_client.get_blob_client(blob_name)
    
        # Download the blob content
        blob_data = blob_client.download_blob().readall()
        
        return blob_data.decode('utf-8')    

    def stream_blob_file(self, container_name, blob_name):    
        print(f"Streaming blob file: {blob_name} from container: {container_name}")
        # Get the container client
        container_client = self.blob_service_client.get_container_client(container_name)   
        # Get the blob client
        blob_client = container_client.get_blob_client(blob_name) 
        # Download blob content

        # Download blob content
        downloader = blob_client.download_blob()
        # Option 1: Read all content at once
        content = downloader.readall()
        #print(content)        
    
    def stream_blob_file2(self, container_name, blob_name):
        print(f"Streaming blob file: {blob_name} from container: {container_name}")

        blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        # Ensure the blob exists before downloading
        if blob_client.exists():
            # Download blob content
            downloader = blob_client.download_blob()
            # Option 1: Read all content at once
            content = downloader.readall().decode('utf-8')   
            print(content)
            # with blob_client.download_blob() as stream:
            #     for line in stream.chunks():
            #         print(line.decode("utf-8"))  
        else:
            print("Blob does not exist!")                          

        # blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        # stream = blob_client.download_blob()
        # return stream
        
        # returning an iterator that yields chunks of data 
        # from a blob in Azure Blob Storage.
        #return stream.chunks()    

    def append_block(self, container_name, blob_name, block: str, header_line: str):
        # Get the container client
        container_client = self.blob_service_client.get_container_client(container_name)
        
        # Get the blob client
        blob_client = container_client.get_blob_client(blob_name)

        # Create the blob if it doesn't exist
        if not blob_client.exists():
            blob_client.create_append_blob()
            blob_client.append_block(header_line)         

        # Append data to the blob       
        blob_client.append_block(block)         