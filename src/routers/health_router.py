from fastapi import APIRouter, Response, HTTPException
from pydantic import BaseModel

from datetime import datetime

router = APIRouter()

#--------------------------------------------------------------------------------
@router.get("")
def health(response: Response):
    """Test if the service is healthy"""

    try:       
        response.status_code = 201
        return {
            "api-name": "claims injestion for dedup api",
            "status": "healthy",
            "invoked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))