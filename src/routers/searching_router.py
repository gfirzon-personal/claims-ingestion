from fastapi import APIRouter, Response, HTTPException
from pydantic import BaseModel

from services import SearchingService

router = APIRouter()

class SimpleSearchRequest(BaseModel):
    index_name: str
    text: str

@router.post("/simple-search")
def test_embeddings(request: SimpleSearchRequest, response: Response):
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