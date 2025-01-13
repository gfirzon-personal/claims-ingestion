from fastapi import APIRouter, Response, HTTPException
from pydantic import BaseModel

from services import ImportService

router = APIRouter()

class ImportRequest(BaseModel):
    index_name: str
    index_type: str
    container_name: str
    blob_name: str
    out_container_name: str
    
#--------------------------------------------------------------------------------
@router.post("/process")
def import_file(request: ImportRequest, response: Response):
    try:
        print(request)

        if not request.index_name or not request.index_type:
            raise HTTPException(status_code=400, detail="Invalid input")     
        
        if not request.container_name or not request.blob_name:
            raise HTTPException(status_code=400, detail="Invalid input")   

        result = ImportService().import_file(
            request.index_name, 
            # request.index_type,
            container_name=request.container_name,
            blob_name=request.blob_name,
            out_container_name=request.out_container_name
            )
        
        response.status_code = 201
        return {
            "message": f"File {request.blob_name} processed for importing", 
            "result": result
            }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    