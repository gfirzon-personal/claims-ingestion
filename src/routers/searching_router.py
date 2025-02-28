from fastapi import APIRouter, Response, HTTPException
from pydantic import BaseModel

from services import SearchingService
from models.PharmaRecord import PharmaRecord

router = APIRouter()

class SimpleSearchRequest(BaseModel):
    index_name: str
    text: str 

class RecordSearchRequest(BaseModel):
    index_name: str
    record: PharmaRecord    

#------------------------------------------------------------------------------------------------
@router.post("/simple-search")
def simple_search(request: SimpleSearchRequest, response: Response):
    try:
        if not request.text or not request.index_name:
            raise HTTPException(status_code=400, detail="Invalid input")

        result = SearchingService().search_vectorized(request.index_name, request.text)
        
        response.status_code = 201
        return {
            "message": f"Searched successfully for {request.text}",
            "response": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#------------------------------------------------------------------------------------------------
@router.post("/record-text-search")
def record_text_search(request: RecordSearchRequest, response: Response):
    try:
        if not request.record or not request.index_name:
            raise HTTPException(status_code=400, detail="Invalid input")

        result = SearchingService(request.index_name).record_search(request.record)
        #result = request.record
        
        response.status_code = 201
        return {
            "message": f"Searched successfully",
            "response": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    
    
#------------------------------------------------------------------------------------------------
@router.post("/hybrid-search")
def hybrid_search(request: SimpleSearchRequest, response: Response):
    try:
        if not request.index_name or not request.text:
            raise HTTPException(status_code=400, detail="Invalid input")

        result = SearchingService(request.index_name).hybrid_search(request.text)
        
        response.status_code = 201
        return {
            "message": f"Searched successfully",
            "response": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))     