import os
import json

from services import BatchCsvParsingService

def get_pharma_docs():
    file_name = "generated_batch_sample.csv"
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)

    batch_csv_parsing_service = BatchCsvParsingService()
    data = batch_csv_parsing_service.get_data(file_path) 

    # List of required attributes
    required_attributes = [
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

    # Filter out the required attributes
    filtered_data = []
    for item in data:
        filtered_item = {key: item[key] for key in required_attributes if key in item}
        filtered_data.append(filtered_item)

    return filtered_data