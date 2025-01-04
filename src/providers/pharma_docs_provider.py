import os
import json

from services import BatchCsvParsingService, StorageService

def get_docs(location: str):
    if location == "local":
        return get_local_docs()
    else:
        return get_blob_docs()

def get_blob_docs():
    print("Getting blob docs")
    container_name = "pharmatest"
    blob_name = "generated_batch_sample.csv"

    try:
        #BatchCsvParsingService()
        StorageService()
    except Exception as e:
        print(e)
    #file_stream = StorageService().stream_blob_file(container_name, blob_name)

    # for chunk in file_stream.chunks():
    #     # Process the chunk (e.g., modify, filter, etc.)
    #     print(chunk)
    #     # processed_chunk = chunk  # Replace with actual processing logic
    #     # yield processed_chunk

def get_required_attributes():
    return [
        "PrescriptionRefNo",
        "PatientFirstName",
        "PatientLastName",
        "PatientDOB",
        "PrescriberID",
        "ProductServiceID",
        "QuantityDispensed",
        "DateRxWritten",
        "DateOfService",
        "DaysSupply",
        "FillNumber",
        "BINNumber",
        "ProcessorControlNo",
        "GroupNo",
        "TransactionCode",
        "OtherCoverageCode",
        "PatientPayAmount",
        "TotalAmountPaid"
    ]

def get_local_docs():
    file_name = "generated_batch_sample.csv"
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)

    batch_csv_parsing_service = BatchCsvParsingService()
    data = batch_csv_parsing_service.get_data(file_path) 

    # List of required attributes
    required_attributes = get_required_attributes()   

    # Filter out the required attributes
    filtered_data = []
    for item in data:
        filtered_item = {key: item[key] for key in required_attributes if key in item}
        filtered_data.append(filtered_item)

    return filtered_data