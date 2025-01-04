from fastapi import APIRouter, Response, HTTPException
from pydantic import BaseModel

from services import IndexLoadingService, StorageService

router = APIRouter()

class LoadIndexRequest(BaseModel):
    index_name: str
    index_type: str
    container_name: str
    blob_name: str

@router.post("/")
def load_index(request: LoadIndexRequest, response: Response):
    try:
        if not request.index_name or not request.index_type:
            raise HTTPException(status_code=400, detail="Invalid input")     
        
        if request.index_type == "pharma" and not request.container_name or not request.blob_name:
            raise HTTPException(status_code=400, details="Invalid input")   

        result = IndexLoadingService().load(
            request.index_name, 
            request.index_type,
            container_name=request.container_name,
            blob_name=request.blob_name
            )
        
        response.status_code = 201
        return {
            "message": "Index loaded successfully", 
            "index_name": request.index_name,
            "result": result
            }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))