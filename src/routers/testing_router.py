from fastapi import APIRouter, Response, HTTPException
from starlette.responses import StreamingResponse
from pydantic import BaseModel

from services import (
    EmbeddingsService, 
    StorageService, 
    BlobClientService)

router = APIRouter()

class EmbedRequest(BaseModel):
    text: str

#------------------------------------------------------------------------------------------------
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

#------------------------------------------------------------------------------------------------
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

#------------------------------------------------------------------------------------------------
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

#------------------------------------------------------------------------------------------------
@router.get("/storage/blobs/{container_name}")
@router.get("/storage/blobs/{container_name}/")
def list_blobs(container_name: str, response: Response):
    try:
        container_names = StorageService().list_files_in_container(container_name)

        response.status_code = 200
        return container_names
    except Exception as e: 
        response.status_code = 500
        return {"error": str(e)}        

#------------------------------------------------------------------------------------------------
@router.get("/storage/blobs/{container_name}/read/{blob_name}")
@router.get("/storage/blobs/{container_name}/read/{blob_name}/")
def read_blob_file(container_name: str, blob_name: str, response: Response):
    try:
        contents = BlobClientService(container_name, blob_name).read_blob_file()

        response.status_code = 200
        return contents
    except Exception as e: 
        response.status_code = 500
        return {"error": str(e)}     

@router.get("/storage/blobs/{container_name}/stream/{blob_name}")
@router.get("/storage/blobs/{container_name}/stream/{blob_name}/")
def stream_blob_file(container_name: str, blob_name: str, response: Response):
    try:
        file_stream = StorageService().stream_blob_file(container_name, blob_name)
        response.status_code = 200
        return StreamingResponse(file_stream, media_type="application/octet-stream")
    except Exception as e:
        response.status_code = 500
        return {"error": str(e)}     

@router.get("/storage/blobs/{container_name}/stream2/{blob_name}")
@router.get("/storage/blobs/{container_name}/stream2/{blob_name}/")
def stream_blob_file(container_name: str, blob_name: str, response: Response):
    try:
        # Process each chunk as it arrives
        for chunk in StorageService().stream_blob_file2(container_name, blob_name):
            #print(chunk.decode('utf-8', errors='ignore'))  # Decode if it's text
            print(f"Received chunk of size {len(chunk)}")        

        response.status_code = 201
        return {
            "message": f"Searched successfully",
            "response": "AAA"
        }
    except Exception as e:
        response.status_code = 500
        return {"error": str(e)}             