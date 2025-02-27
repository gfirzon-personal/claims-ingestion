import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import (health_router,
    index_schema_router, 
    index_data_router, 
    import_router,
    searching_router,
    documents_router,
    testing_router,
    parser_router)

app = FastAPI(title = "claims injestion for dedup api", description = "tbd", version = "0.1")

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
 
app.include_router(health_router.router, prefix = "/health", tags = ["health"])
app.include_router(index_schema_router.router, prefix = "/index-schema", tags = ["index-schema"])
app.include_router(index_data_router.router, prefix = "/index-data", tags = ["index-data"])
app.include_router(import_router.router, prefix = "/importing", tags = ["importing"])
app.include_router(searching_router.router, prefix = "/searching", tags = ["searching"])
app.include_router(documents_router.router, prefix = "/documents", tags = ["documents"])
app.include_router(testing_router.router, prefix = "/testing", tags = ["testing"])
app.include_router(parser_router.router, prefix = "/parser", tags = ["parser"])

if __name__ == "__main__":
    import uvicorn  
    uvicorn.run(app, host = "0.0.0.0", port = 8000)