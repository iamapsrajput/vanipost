from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.db.database import get_db

router = APIRouter()


@router.get("/")
async def get_posts(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    """Get all posts with pagination"""
    # TODO: Implement when Post model is created
    return {"posts": [], "total": 0, "skip": skip, "limit": limit}


@router.post("/")
async def create_post(db: AsyncSession = Depends(get_db)):
    """Create a new post"""
    # TODO: Implement when Post model and schema are created
    return {"message": "Post creation endpoint - to be implemented"}


@router.get("/{post_id}")
async def get_post(post_id: int, db: AsyncSession = Depends(get_db)):
    """Get a specific post by ID"""
    # TODO: Implement when Post model is created
    return {"message": f"Get post {post_id} - to be implemented"}


@router.put("/{post_id}")
async def update_post(post_id: int, db: AsyncSession = Depends(get_db)):
    """Update a specific post"""
    # TODO: Implement when Post model and schema are created
    return {"message": f"Update post {post_id} - to be implemented"}


@router.delete("/{post_id}")
async def delete_post(post_id: int, db: AsyncSession = Depends(get_db)):
    """Delete a specific post"""
    # TODO: Implement when Post model is created
    return {"message": f"Delete post {post_id} - to be implemented"}
