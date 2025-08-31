from fastapi import APIRouter
from .endpoints import health, posts

api_router = APIRouter()

api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
