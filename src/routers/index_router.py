from fastapi import APIRouter, Response

router = APIRouter()

@router.get("/")
@router.get("/")
def foo (response: Response):
    data = {
        'message': "Hello World"
    }

    response.status_code = 200
    return data