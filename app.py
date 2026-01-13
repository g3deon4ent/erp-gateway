from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.config import get_settings

# Import routers here
# Example: from routes.your_module import router as your_router

settings = get_settings()

# Initialize FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
    docs_url="/docs" if settings.env == "development" else None,
    redoc_url="/redoc" if settings.env == "development" else None,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """
    Root endpoint - Health check
    """
    return {
        "message": "Welcome to FastAPI ERP",
        "version": settings.app_version,
        "environment": settings.env
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "environment": settings.env
    }


# Include routers here
# Example: app.include_router(your_router, prefix=settings.api_prefix)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug
    )