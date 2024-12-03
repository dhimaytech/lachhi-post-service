from uuid import uuid4
from sqlalchemy import Column, DateTime, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from pydantic import BaseModel
from configurations.database import Base


# SQLAlchemy Model
class UserGroupDB(Base):
    __tablename__ = "user_groups"

    user_group_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    group_id = Column(UUID(as_uuid=True), ForeignKey('groups.group_id'), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    __table_args__ = (
        Index('idx_user_groups_user_id', 'user_id'),
    )


# Pydantic Models for API
class UserGroupBase(BaseModel):
    user_id: UUID
    group_id: UUID

class UserGroupCreate(UserGroupBase):
    pass

class UserGroup(UserGroupBase):
    user_group_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
