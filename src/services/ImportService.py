import uuid
from services import SearchingService
from models.PharmaRecord import PharmaRecord

from services.StorageService import StorageService
from services.BatchCsvParsingService import BatchCsvParsingService

from providers.pharma_docs_provider import (
    get_docs, 
    get_blob_docs, 
    get_required_attributes)

class ImportService:
    """Service to import data"""
    def __init__(self):
        pass

    def import_file(self, index_name: str, container_name:str, blob_name:str):
        content = StorageService().read_blob_file(container_name, blob_name)
        data_list = BatchCsvParsingService().get_data_from_content(content)

        filtered_data = self.filter(data_list)

        for doc in filtered_data:
            doc["id"] = str(uuid.uuid4())  # Add GUID as string to the document
            
            pharma_record = PharmaRecord.from_dict(doc)  # Convert doc to PharmaRecord object
            result = SearchingService().record_search(index_name, pharma_record)
            print(result["result_count"])

        return filtered_data
       
    def filter(self, data):
        # List of required attributes
        required_attributes = get_required_attributes()       

        filtered_data = []
        for item in data:
            filtered_item = {key: item[key] for key in required_attributes if key in item}
            filtered_data.append(filtered_item)

        return filtered_data         
        