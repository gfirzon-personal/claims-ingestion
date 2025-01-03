from factories.BlobServiceClientFactory import BlobServiceClientFactory

class StorageService:
    def __init__(self):
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