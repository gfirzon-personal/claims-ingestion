from fastapi import APIRouter, Response, HTTPException
from pydantic import BaseModel

from services import IndexDataService

router = APIRouter()

#--------------------------------------------------------------------------------
@router.get("/index/{index_name}")
def get_documents(index_name: str,  response: Response):
    """Retrieve all documents from the"""
    try:
        if not index_name:
            raise HTTPException(status_code=400, detail="Invalid input")   

        docs = IndexDataService(index_name).get_all_docs()
        
        response.status_code = 201
        return {
            "index": index_name,
            "result": docs
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#--------------------------------------------------------------------------------
@router.get("/index/{index_name}/id/{doc_id}")
def get_doc_by_id(index_name: str, doc_id: str,  response: Response):
    """Retrieve a document from the index by ID"""
    try:
        if not index_name:
            raise HTTPException(status_code=400, detail="Invalid input")   

        docs = IndexDataService(index_name).get_doc_by_id(doc_id)
        
        response.status_code = 201
        return {
            "index": index_name,
            "result": docs
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    
    
#--------------------------------------------------------------------------------
@router.delete("/index/{index_name}/id/{doc_id}")
def delete_doc_by_id(index_name: str, doc_id: str,  response: Response):
    """Delete a document from the index by ID"""
    try:
        if not index_name:
            raise HTTPException(status_code=400, detail="Invalid input")   

        docs = IndexDataService(index_name).delete_doc_by_id(doc_id)
        
        response.status_code = 201
        return {
            "index": index_name,
            "result": docs
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))       

#--------------------------------------------------------------------------------
@router.post("/index/{index_name}/")
def add_document(index_name: str, request: dict, response: Response):
    """Add a document to the index"""
    try:
        if not index_name:
            raise HTTPException(status_code=400, detail="Invalid input")   

        doc_id = IndexDataService(index_name).add_document(request)
        
        response.status_code = 201
        return {
            "index": index_name,
            "result": doc_id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    