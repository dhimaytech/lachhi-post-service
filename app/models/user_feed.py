from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from pydantic import BaseModel
from configurations.database import Base


class UserFeedDB(Base):
    __tablename__ = "user_feeds"

    user_feed_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    post_id = Column(UUID(as_uuid=True), ForeignKey('posts.post_id'), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())


class UserFeedBase(BaseModel):
    user_id: UUID
    post_id: UUID

class UserFeedCreate(UserFeedBase):
    pass

class UserFeed(UserFeedBase):
    user_feed_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
