from factories.BlobServiceClientFactory import BlobServiceClientFactory

class StorageService:
    def __init__(self):
        self.storage_service = BlobServiceClientFactory().create()

    def list_container_names(self):
        container_names = []
        containers = self.storage_service.list_containers()
        for container in containers:
            container_names.append(container['name'])
        return container_names        