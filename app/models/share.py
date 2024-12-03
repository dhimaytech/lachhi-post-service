from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from pydantic import BaseModel
from configurations.database import Base


class ShareDB(Base):
    __tablename__ = "shares"

    share_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    post_id = Column(UUID(as_uuid=True), ForeignKey('posts.post_id'), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    group_id = Column(UUID(as_uuid=True), ForeignKey('groups.group_id'), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())


class ShareBase(BaseModel):
    post_id: UUID
    group_id: UUID | None = None

class ShareCreate(ShareBase):
    pass

class Share(ShareBase):
    share_id: UUID
    user_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
