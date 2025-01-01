from fastapi import APIRouter, Response, HTTPException
from pydantic import BaseModel

from services import IndexSchemaService

router = APIRouter()

class CreateIndexRequest(BaseModel):
    index_name: str
    vector_search_profile_name: str
    algorithm_configuration_name: str

#--------------------------------------------------------------------------------
@router.get("/")
def create_item(response: Response):
    try:
        indexes = IndexSchemaService().list_indexes()
        
        response.status_code = 201
        return {
            "result": indexes
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#--------------------------------------------------------------------------------
@router.post("/")
def create_item(request: CreateIndexRequest, response: Response):
    try:
        if not request.index_name or not request.vector_search_profile_name or not request.algorithm_configuration_name:
            raise HTTPException(status_code=400, detail="Invalid input")
        
        IndexSchemaService().create_index_with_vector_field(
            request.index_name, 
            request.vector_search_profile_name, 
            request.algorithm_configuration_name)
        
        response.status_code = 201
        return {"message": "Index created successfully", "index_name": request.index_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/drop/{index_name}")
def create_item(index_name: str, response: Response):
    try:
        if not index_name:
            raise HTTPException(status_code=400, detail="Invalid input")
        
        IndexSchemaService().delete_index(index_name)
        
        response.status_code = 201
        return {"message": "Index deleted successfully", "index_name": index_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    