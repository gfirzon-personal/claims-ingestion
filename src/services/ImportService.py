import uuid
import logging
from datetime import datetime
from services import SearchingService
from models.PharmaRecord import PharmaRecord

from services.BlobClientService import BlobClientService
from services.BatchCsvParsingService import BatchCsvParsingService

from providers.pharma_docs_provider import (
    get_docs, 
    get_blob_docs, 
    get_required_attributes)

#--------------------------------------------------------------------------------
class ImportService:
    """Service to import data"""

    #--------------------------------------------------------------------------------
    def __init__(self):
        ...
    
    #--------------------------------------------------------------------------------
    def import_file(self, index_name: str, container_name: str, blob_name: str, out_container_name: str):
        content = BlobClientService(container_name, blob_name).read_blob_file()

        rl = BatchCsvParsingService().read_all_lines(content)

        # Generate a timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        out_dupe_blob_name = f"out_dupes_{timestamp}.csv"        
        out_new_blob_name = f"out_new_{timestamp}.csv"

        header_line = rl["header_line"] + '\n'
        searching_service = SearchingService(index_name)

        # Print the count of elements in result_list
        #print(f"Count of elements in result_list: {len(rl['result_list'])}")

        new_rec_count = 0
        dup_rec_count = 0

        dupe_rec_client = BlobClientService(out_container_name, out_dupe_blob_name)
        new_rec_client = BlobClientService(out_container_name, out_new_blob_name)

        for item in rl["result_list"]:
            line = item["line"]
            record = item["record"]
            pharma_record = PharmaRecord.from_dict(record)
            search_result = searching_service.record_search(pharma_record)  
            #print("search_result count", search_result["result_count"] ) 

            if search_result["result_count"] == 0:
                new_rec_count += 1
                new_rec_client.append_block(line, header_line)
            else:
                dup_rec_count += 1
                dupe_rec_client.append_block(line, header_line)

        return {
            "new_rec_count": new_rec_count,
            "dup_rec_count": dup_rec_count,
            "total_rec_count": new_rec_count + dup_rec_count
        }    
       
    #--------------------------------------------------------------------------------
    def filter(self, data):
        # List of required attributes
        required_attributes = get_required_attributes()       

        filtered_data = []
        for item in data:
            filtered_item = {key: item[key] for key in required_attributes if key in item}
            filtered_data.append(filtered_item)

        return filtered_data         
        