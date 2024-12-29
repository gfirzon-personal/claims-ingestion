import os
import json
from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

from services import BatchCsvParsingService

router = APIRouter()

@router.get("/headers/")
@router.get("/headers")
def get_headers(response: Response):
    try:
        file_name = "generated_batch_sample.csv"
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)
        batch_csv_parsing_service = BatchCsvParsingService()
        headers = batch_csv_parsing_service.get_headers(file_path)

        response.status_code = 200
        return headers
    except Exception as e: 
        response.status_code = 500
        return {"error": str(e)}    
    
@router.get("/data/")
@router.get("/data")
def get_data(response: Response):
    try:
        file_name = "generated_batch_sample.csv"
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)
        batch_csv_parsing_service = BatchCsvParsingService()
        data = batch_csv_parsing_service.get_data(file_path)

        response.status_code = 200
        return data
    except Exception as e: 
        response.status_code = 500
        return {"error": str(e)}        