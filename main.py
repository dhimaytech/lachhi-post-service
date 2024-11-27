from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
import uvicorn
from app.models import Post

# Initialize FastAPI app
app = FastAPI(
    title="lachhi-post-service",
    description="service for managing posts in lachhi",
    version="1.0.0"
)

# Routes
@app.get("/")
def root() -> Dict[str, str]:
    return {"status": "healthy", "message": "Lachhi Post Service is running"}

@app.get("/health")
def health_check() -> Dict[str, str]:
    return {"status": "healthy"}

# Error Handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"detail": exc.detail, "status_code": exc.status_code}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
