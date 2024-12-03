from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from pydantic import BaseModel
from configurations.database import Base

# SQLAlchemy Model
class GroupAdminDB(Base):
    __tablename__ = "group_admins"
    
    group_admin_id = Column(UUID, primary_key=True, default=uuid4)
    group_id = Column(UUID, ForeignKey("groups.group_id"))
    user_id = Column(UUID, ForeignKey("users.user_id"))
    is_app_admin = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

# Pydantic Models
class GroupAdminBase(BaseModel):
    group_id: UUID
    user_id: UUID
    is_app_admin: bool

class GroupAdminCreate(GroupAdminBase):
    pass

class GroupAdmin(GroupAdminBase):
    group_admin_id: UUID
    created_at: datetime
    
    class Config:
        from_attributes = True
