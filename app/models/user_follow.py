from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from pydantic import BaseModel
from configurations.database import Base


class UserFollowDB(Base):
    __tablename__ = "user_follows"

    follow_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    follower_user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    followed_user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    __table_args__ = (
        Index('idx_user_follows_follower', 'follower_user_id'),
        Index('idx_user_follows_followed', 'followed_user_id'),
    )


class UserFollowBase(BaseModel):
    followed_user_id: UUID

class UserFollowCreate(UserFollowBase):
    pass

class UserFollow(UserFollowBase):
    follow_id: UUID
    follower_user_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
