from fastapi import APIRouter, Response, HTTPException
from pydantic import BaseModel

from services import EmbeddingsService

router = APIRouter()

class SimpleSearchRequest(BaseModel):
    text: str

@router.post("/simple-search")
def test_embeddings(request: SimpleSearchRequest, response: Response):
    try:
        if not request.text :
            raise HTTPException(status_code=400, detail="Invalid input")

        #embeddings = EmbeddingsService().get_embeddings(request.text)
        
        response.status_code = 201
        return {"message": f"Searched successfully for {request.text}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))