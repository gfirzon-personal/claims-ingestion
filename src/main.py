from fastapi import FastAPI
from routers import index_router

app = FastAPI(title = "dedup api")
 
app.include_router(index_router.router, prefix = "/indexes", tags = ["indexes"])

if __name__ == "__main__":
    import uvicorn  
    uvicorn.run(app, host = "0.0.0.0", port = 8000)