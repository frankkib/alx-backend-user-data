#!/usr/bin/env python3
"""Class base user module
"""
from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """The user class inheriting from Base
    """
    __tablename__ = 'users'
    id: int = Column(Integer, primary_key=True)
    email:str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str = Column(String(250), nullable=False)
    reset_token: str = Column(String(250), nullable=True)
