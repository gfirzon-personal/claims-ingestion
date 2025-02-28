import logging
import csv
from io import StringIO
import uuid
from factories.SearchClientFactory import SearchClientFactory
from services.EmbeddingsService import EmbeddingsService
from services.StorageService import StorageService
from services.BatchCsvParsingService import BatchCsvParsingService
from services.BlobClientService import BlobClientService

from providers.pharma_docs_provider import (get_required_attributes)

class IndexLoadingService:
    """Service to load data into the search index from a blob storage"""
    def __init__(self):
        pass

    def __process_csv_chunks(self, stream):
        # Process each chunk as it arrives
        buffer = ""
        for chunk in stream:
            buffer += chunk.decode('utf-8')
            while '\n' in buffer:
                line, buffer = buffer.split('\n', 1)
                yield line
        if buffer:
            yield buffer     

    def __load_data_from_blob_stream(self, container_name: str, blob_name: str):    
        blob_client_service = BlobClientService(container_name, blob_name)

        line_count = 0
        for line in self.__process_csv_chunks(blob_client_service.stream_blob_file(container_name, blob_name)):
            line_count += 1                  
            # if line_count % 1000 == 0:
            #     print(f"Received lines {line_count}")

            self.process_csv_line(line, line_count)
        print(f"Received lines {line_count}")
        return line_count - 1 # Exclude the header line    

    @staticmethod
    def convert_csv_line_to_array(csv_line):
        csv_reader = csv.reader(StringIO(csv_line))
        return next(csv_reader)

    def process_csv_line(self, csv_line: str, line_count: int):
        """Process a line of a CSV file"""
        #print(f"Processing line: {line}") 
        line = IndexLoadingService.convert_csv_line_to_array(csv_line) 
        
        # if line 1 its a header line
        if line_count == 1:
            self.header_line = line
        else:
            # convert line to dictionary  
            record = dict(zip(self.header_line, line))
            doc = self.filter_one(record)
            doc["id"] = str(uuid.uuid4())  # Add GUID as string to the document    
            result = self.search_client.upload_documents(documents=[doc])                    

    def load(self, index_name: str, index_type: str, container_name: str, blob_name: str, stream_mode: bool = False):
        """Load data into the search index from a blob storage"""

        logging.info(f"Loading data from blob: container_name={container_name}, blob_name={blob_name}")
        self.search_client = SearchClientFactory().create(index_name)

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
            if stream_mode:
                # Load data from blob storage from stream
                count = self.__load_data_from_blob_stream(container_name, blob_name)
                return count
                #return "Data loaded successfully"
            else:
                content = BlobClientService(container_name, blob_name).read_blob_file()
                logging.info(f"Retrieved content from blob: container_name={container_name}, blob_name={blob_name} - {len(content)} bytes")

                data_list = BatchCsvParsingService().get_data_from_content(content)
                filtered_data = self.filter(data_list)

                embedding_service = EmbeddingsService()
                for doc in filtered_data:
                    doc["content"] = IndexLoadingService.concatenate_doc_values(doc)
                    doc["id"] = str(uuid.uuid4())  # Add GUID as string to the document

                    embedding = embedding_service.get_embeddings(doc["content"]).tolist()
                    doc["content_vector"] = embedding  # Add embedding to the document

                result = self.search_client.upload_documents(documents=filtered_data)
                return len(filtered_data)

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
        return ' | '.join(str(value) for value in doc.values())
    
    def filter(self, data):
        # List of required attributes
        required_attributes = get_required_attributes()       

        filtered_data = []
        for item in data:
            filtered_item = {key: item[key] for key in required_attributes if key in item}
            filtered_data.append(filtered_item)

        return filtered_data   

    def filter_one(self, item):
        # List of required attributes
        required_attributes = get_required_attributes()       

        filtered_item = {key: item[key] for key in required_attributes if key in item}
        return filtered_item
