"""
SQLAlchemy Domain Models (ORM)
Course, Module, Material, UserProgress, and User
"""
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime
from Back_End.database.connection import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    order_index = Column(Integer, default=1)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    modules = relationship("Module", back_populates="course", cascade="all, delete-orphan", order_by="Module.order_index")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "slug": self.slug,
            "description": self.description,
            "order_index": self.order_index,
            "is_active": self.is_active,
            "modules_count": len(self.modules) if self.modules else 0
        }

class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    order_index = Column(Integer, default=1)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    course = relationship("Course", back_populates="modules")
    materials = relationship("Material", back_populates="module", cascade="all, delete-orphan", order_by="Material.chapter_number")

    def to_dict(self):
        return {
            "id": self.id,
            "course_id": self.course_id,
            "name": self.name,
            "slug": self.slug,
            "description": self.description,
            "order_index": self.order_index,
            "is_active": self.is_active,
            "materials_count": len(self.materials) if self.materials else 0
        }

class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, autoincrement=True)
    module_id = Column(Integer, ForeignKey("modules.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
    chapter_number = Column(Integer, default=1)
    is_checkpoint = Column(Boolean, default=False)
    prerequisite_id = Column(Integer, ForeignKey("materials.id", ondelete="SET NULL"), nullable=True)
    summary = Column(Text, nullable=True)
    content = Column(Text, nullable=True)
    order_index = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    module = relationship("Module", back_populates="materials")
    prerequisite = relationship("Material", remote_side=[id], backref="next_materials")
    progress_records = relationship("UserProgress", back_populates="material", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "module_id": self.module_id,
            "title": self.title,
            "slug": self.slug,
            "chapter_number": self.chapter_number,
            "is_checkpoint": self.is_checkpoint,
            "prerequisite_id": self.prerequisite_id,
            "summary": self.summary,
            "order_index": self.order_index
        }

class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    material_id = Column(Integer, ForeignKey("materials.id", ondelete="CASCADE"), nullable=True)
    topic_id = Column(Integer, nullable=True)
    status = Column(SQLEnum('Locked', 'In_Progress', 'Completed', name='progress_status'), default='Locked')
    score = Column(Integer, default=0)
    current_stage = Column(Integer, default=0)
    attempts_count = Column(Integer, default=0)
    time_spent_seconds = Column(Integer, default=0)
    completed_at = Column(DateTime, nullable=True)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    material = relationship("Material", back_populates="progress_records")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "material_id": self.material_id,
            "status": self.status,
            "score": self.score,
            "current_stage": self.current_stage,
            "attempts_count": self.attempts_count,
            "time_spent_seconds": self.time_spent_seconds,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "last_updated": self.last_updated.isoformat() if self.last_updated else None
        }

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    photo = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "photo": self.photo
        }
