import uuid
from factories.SearchClientFactory import SearchClientFactory
from services.EmbeddingsService import EmbeddingsService
from services.StorageService import StorageService
from services.BatchCsvParsingService import BatchCsvParsingService

from providers.pharma_docs_provider import (
    get_docs, 
    get_blob_docs, 
    get_required_attributes)

class IndexLoadingService:
    def __init__(self):
        pass

    def load(self, index_name:str, index_type:str, container_name:str, blob_name:str):
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
            content = StorageService().read_blob_file(container_name, blob_name)
            data_list = BatchCsvParsingService().get_data_from_content(content)
            filtered_data = self.filter(data_list)

            for doc in filtered_data:
                doc["id"] = str(uuid.uuid4())  # Add GUID as string to the document

            result = search_client.upload_documents(documents=filtered_data)
            return result

            #print(filtered_data)
            # content_array = content.split('\n')  # Split content into an array based on new lines
            # # Now you can process each line in content_array
            # header_line = content_array[0]
            # # Skip the first element which is the header using slicing
            # for line in content_array[1:]:  
            #     #print(line)  # Or any other processing you need to do
            #     self.build_document(header_line, line)
            # result = None            
            # with StorageService().stream_blob_file("pharmatest", "generated_batch_sample.csv") as stream:
            #     for line in stream.chunks():
            #         print(line.decode("utf-8"))
            result = None

            #print(f"Total number of chunks: {chunk_count}")
            return result
            # for chunk in get_blob_docs():
            #     # Here you can handle each processed chunk
            #     print(chunk)  # Replace with actual handling logic
            #print ("Loading data from blob storage")

            # documents = get_docs("azure")
            # for doc in documents:
            #     doc["id"] = str(uuid.uuid4())  # Add GUID as string to the document
                # Generate embedding for the 'description' field
                #embedding = model.encode(doc["description"]).tolist()
                #embedding = EmbeddingsService().get_embeddings(doc["content"]).tolist()

                #doc["content_vector"] = embedding  # Add embedding to the document    
                
                # For exact searches, traditional keyword-based search works better. 
                # However, vector search can complement exact search by finding documents 
                # with semantically similar meanings even if exact matches are missing.        

        #result = search_client.upload_documents(documents=documents)
        
        #return result
    
    def concatenate_doc_values(doc):
        return ''.join(str(value) for value in doc.values())
    
    def filter(self, data):
        # List of required attributes
        required_attributes = get_required_attributes()       

        filtered_data = []
        for item in data:
            filtered_item = {key: item[key] for key in required_attributes if key in item}
            filtered_data.append(filtered_item)

        return filtered_data            
