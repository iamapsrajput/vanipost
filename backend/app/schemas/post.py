from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any


class PostBase(BaseModel):
    title: str
    content: str
    platform: str
    scheduled_at: Optional[datetime] = None
    post_metadata: Optional[Dict[str, Any]] = None


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    platform: Optional[str] = None
    status: Optional[str] = None
    scheduled_at: Optional[datetime] = None
    post_metadata: Optional[Dict[str, Any]] = None


class PostResponse(PostBase):
    id: int
    status: str
    published_at: Optional[datetime] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
