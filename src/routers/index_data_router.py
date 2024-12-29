from fastapi import APIRouter, Response, HTTPException
from pydantic import BaseModel

from services import IndexLoadingService

router = APIRouter()

class LoadIndexRequest(BaseModel):
    index_name: str

@router.post("/")
def load_index(request: LoadIndexRequest, response: Response):
    try:
        if not request.index_name :
            raise HTTPException(status_code=400, detail="Invalid input")
        
        documents = [
            {"id": "1", "content": "This is the first document."},
            {"id": "2", "content": "This is the second document."}
        ]
        
        result = IndexLoadingService().load(
            request.index_name, 
            documents)
        
        response.status_code = 201
        return {
            "message": "Index loaded successfully", 
            "index_name": request.index_name,
            "result": result
            }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))