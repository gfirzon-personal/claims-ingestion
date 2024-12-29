from factories.SearchClientFactory import SearchClientFactory

class IndexLoadingService:
    def __init__(self):
        pass

    def load(self, index_name:str, documents):
        search_client = SearchClientFactory().create(index_name)
        result = search_client.upload_documents(documents=documents)
        
        return result