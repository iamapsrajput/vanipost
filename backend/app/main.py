from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import redis.asyncio as redis
from .core.config import settings
from .api.v1.api import api_router
from .db.database import engine
from .db.base import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Setup Redis connection
    app.state.redis = redis.from_url(settings.REDIS_URL)

    yield

    # Shutdown
    await app.state.redis.close()


app = FastAPI(
    title="VaniPost API", description="Social media automation platform API", version="0.1.0", lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "VaniPost API is running"}
