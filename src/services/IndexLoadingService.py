import uuid
from factories.SearchClientFactory import SearchClientFactory
from services.EmbeddingsService import EmbeddingsService

from providers.pharma_docs_provider import get_pharma_docs

class IndexLoadingService:
    def __init__(self):
        pass

    def load(self, index_name:str, index_type:str):
        search_client = SearchClientFactory().create(index_name)

        if index_type == "test":
            documents = [
                {"id": "1", "content": "This is the first document."},
                {"id": "2", "content": "This is the second document."}
            ]
            # Generate Embeddings and Populate Data
            for doc in documents:
                #embedding = model.encode(doc["description"]).tolist()
                embedding = EmbeddingsService().get_embeddings(doc["content"]).tolist()

                doc["content_vector"] = embedding  # Add embedding to the document
        else:
            documents = get_pharma_docs()
            for doc in documents:
                doc["id"] = str(uuid.uuid4())  # Add GUID as string to the document
                # Generate embedding for the 'description' field
                #embedding = model.encode(doc["description"]).tolist()
                #embedding = EmbeddingsService().get_embeddings(doc["content"]).tolist()

                #doc["content_vector"] = embedding  # Add embedding to the document    
                
                # For exact searches, traditional keyword-based search works better. 
                # However, vector search can complement exact search by finding documents 
                # with semantically similar meanings even if exact matches are missing.        

        result = search_client.upload_documents(documents=documents)
        
        return result
    
    def concatenate_doc_values(doc):
        return ''.join(str(value) for value in doc.values())
