from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, Text, String, DateTime, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from pydantic import BaseModel
from configurations.database import Base


class PostMediaDB(Base):
    __tablename__ = "post_media"

    media_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    post_id = Column(UUID(as_uuid=True), ForeignKey('posts.post_id'), nullable=False)
    media_url = Column(Text, nullable=False)
    media_type = Column(String(50), nullable=False)  # image, video, audio
    created_at = Column(DateTime, nullable=False, server_default=func.now())


class PostMediaBase(BaseModel):
    media_url: str
    media_type: str

class PostMediaCreate(PostMediaBase):
    post_id: UUID

class PostMedia(PostMediaBase):
    media_id: UUID
    post_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
