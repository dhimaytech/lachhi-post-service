from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Index, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from pydantic import BaseModel
from configurations.database import Base


class LikeDB(Base):
    __tablename__ = "likes"

    like_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    post_id = Column(UUID(as_uuid=True), ForeignKey('posts.post_id'), nullable=True)
    comment_id = Column(UUID(as_uuid=True), ForeignKey('comments.comment_id'), nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    __table_args__ = (
        CheckConstraint('NOT (post_id IS NULL AND comment_id IS NULL)', name='check_like_target'),
        CheckConstraint('NOT (post_id IS NOT NULL AND comment_id IS NOT NULL)', name='check_like_single_target'),
        Index('idx_likes_post_id', 'post_id'),
        Index('idx_likes_comment_id', 'comment_id'),
    )


class LikeBase(BaseModel):
    post_id: UUID | None = None
    comment_id: UUID | None = None

class LikeCreate(LikeBase):
    pass

class Like(LikeBase):
    like_id: UUID
    user_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
