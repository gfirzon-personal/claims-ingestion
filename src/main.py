from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import index_schema_router, index_data_router, parser_router

app = FastAPI(title = "dedup api")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
 
app.include_router(index_schema_router.router, prefix = "/index-schema", tags = ["index-schema"])
app.include_router(index_data_router.router, prefix = "/index-data", tags = ["index-data"])
app.include_router(parser_router.router, prefix = "/parser", tags = ["parser"])

if __name__ == "__main__":
    import uvicorn  
    uvicorn.run(app, host = "0.0.0.0", port = 8000)