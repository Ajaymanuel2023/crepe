from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import engine, Base
from app.api.v1.endpoints import restaurants

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A Zomato clone backend API with PostgreSQL",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(
    restaurants.router,
    prefix=f"{settings.API_V1_STR}/restaurants",
    tags=["restaurants"]
)

# Health check endpoints
@app.get("/")
async def root():
    return {
        "message": "Zomato Clone API is running with PostgreSQL!",
        "version": "1.0.0",
        "database": "Neon PostgreSQL",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "connected"}