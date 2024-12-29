from factories.SearchClientFactory import SearchClientFactory
from services.EmbeddingsService import EmbeddingsService

class IndexLoadingService:
    def __init__(self):
        pass

    def load(self, index_name:str, documents):
        search_client = SearchClientFactory().create(index_name)

        # Generate Embeddings and Populate Data
        for doc in documents:
            # Generate embedding for the 'description' field
            #embedding = model.encode(doc["description"]).tolist()
            embedding = EmbeddingsService().get_embeddings(doc["content"]).tolist()

            doc["content_vector"] = embedding  # Add embedding to the document

        result = search_client.upload_documents(documents=documents)
        
        return result