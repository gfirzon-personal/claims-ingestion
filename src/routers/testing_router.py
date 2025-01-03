from fastapi import APIRouter, Response, HTTPException
from pydantic import BaseModel

from services import EmbeddingsService, StorageService

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
    
@router.get("/env/")
@router.get("/env")
def get_env_entries(response: Response):
    try:
        from utils import config

        config_dict = config.load_env_as_dict('.env')

        response.status_code = 200
        return config_dict
    except Exception as e: 
        response.status_code = 500
        return {"error": str(e)}       

@router.get("/storage/")
@router.get("/storage")
def list_containers(response: Response):
    try:
        container_names = StorageService().list_container_names()

        response.status_code = 200
        return container_names
    except Exception as e: 
        response.status_code = 500
        return {"error": str(e)}         