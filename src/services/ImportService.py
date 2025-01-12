import uuid
from datetime import datetime
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

    def import_file_orig(self, index_name: str, container_name:str, blob_name:str):
        content = StorageService().read_blob_file(container_name, blob_name)
        data_list = BatchCsvParsingService().get_data_from_content(content)
        searching_service = SearchingService(index_name)

        filtered_data = self.filter(data_list)

        for doc in filtered_data:
            doc["id"] = str(uuid.uuid4())  # Add GUID as string to the document
            
            pharma_record = PharmaRecord.from_dict(doc)  # Convert doc to PharmaRecord object
            result = searching_service.record_search(pharma_record)
            print(result["result_count"])

        return filtered_data    

    def import_file_2(self, index_name: str, container_name:str, blob_name:str):
        content = StorageService().read_blob_file(container_name, blob_name)
        file_lines = BatchCsvParsingService().get_data_from_content(content)
        searching_service = SearchingService(index_name)

        out_container_name = "result-files"
        # Generate a timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        out_dupe_blob_name = f"out_dupe_blob_{timestamp}.csv"

        pharma_lines = []
        for line in file_lines:
            pharma_record = PharmaRecord.from_dict(line)
            pharma_lines.append(pharma_record)

            result = searching_service.record_search(pharma_record)   
            if result["result_count"] > 0:
                # save record to blob storage for manual review
                StorageService().append_block(out_container_name, out_dupe_blob_name, line)
                pass
            else:
                # save record to blob storage for manual review
                pass

            #print(result["result_count"])

        return pharma_lines
    
    def import_file(self, index_name: str, container_name:str, blob_name:str):
        content = StorageService().read_blob_file(container_name, blob_name)

        rl = BatchCsvParsingService().read_all_lines(content)

        out_container_name = "result-files"
        # Generate a timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        out_dupe_blob_name = f"out_dupes_{timestamp}.csv"        
        out_new_blob_name = f"out_new_{timestamp}.csv"

        header_line = rl["header_line"] + '\n'
        searching_service = SearchingService(index_name)

        # Print the count of elements in result_list
        #print(f"Count of elements in result_list: {len(rl['result_list'])}")

        for item in rl["result_list"]:
            line = item["line"]
            record = item["record"]
            pharma_record = PharmaRecord.from_dict(record)
            search_result = searching_service.record_search(pharma_record)  
            #print("search_result count", search_result["result_count"] ) 

            if search_result["result_count"] == 0:
                print("new rec found")
                StorageService().append_block(out_container_name, out_new_blob_name, line, header_line)
            else:
                print("dup rec found")
                StorageService().append_block(out_container_name, out_dupe_blob_name, line, header_line)

        return "done"    
       
    def filter(self, data):
        # List of required attributes
        required_attributes = get_required_attributes()       

        filtered_data = []
        for item in data:
            filtered_item = {key: item[key] for key in required_attributes if key in item}
            filtered_data.append(filtered_item)

        return filtered_data         
        