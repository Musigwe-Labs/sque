from database import engine
from sqlalchemy import Column, ForeignKey, Integer, Boolean, String
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime, timezone, timedelta
import uuid
from sqlalchemy.types import Text, JSON
import sqlalchemy
from enum import Enum

class User(SQLModel, table=True):
    id: int = Field(index=True, primary_key=True)
    wallet: str = Field(unique=True)
    points: float = Field(default=1000.0)
    referral_id: str = Field(nullable=True)
    referral_count: int =Field(default=0)
    tasks: int = Field(default=0)
    ftwitter: bool = Field(default=False)
    ftelegram_comm: bool = Field(default=False)
    f_telegram_channel: bool = Field(default=False)
    likes: bool = Field(default=False)
    rt_link: str
    tg_username: str






def create_db_and_tables():
    SQLModel.metadata.create_all(engine)