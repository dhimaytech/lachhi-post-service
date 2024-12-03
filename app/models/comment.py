from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, Text, DateTime, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from pydantic import BaseModel
from configurations.database import Base


class CommentDB(Base):
    __tablename__ = "comments"

    comment_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    post_id = Column(UUID(as_uuid=True), ForeignKey('posts.post_id'), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    parent_comment_id = Column(UUID(as_uuid=True), ForeignKey('comments.comment_id'), nullable=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        Index('idx_comments_post_id', 'post_id'),
    )


class CommentBase(BaseModel):
    content: str
    parent_comment_id: UUID | None = None

class CommentCreate(CommentBase):
    post_id: UUID

class Comment(CommentBase):
    comment_id: UUID
    post_id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime | None

    class Config:
        from_attributes = True
