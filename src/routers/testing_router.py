from fastapi import APIRouter, Response, HTTPException
from pydantic import BaseModel

from services import EmbeddingsService

router = APIRouter()

class EmbedRequest(BaseModel):
    text: str

@router.post("/embeddings")
def test_embeddings(request: EmbedRequest, response: Response):
    try:
        if not request.text :
            raise HTTPException(status_code=400, detail="Invalid input")

        embeddings = EmbeddingsService().get_embeddings(request.text)
        
        response.status_code = 201
        return {"message": "Embedded successfully", "embeddings": embeddings.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))