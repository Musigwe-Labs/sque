from database import engine
from sqlalchemy import Column, ForeignKey, Integer, Boolean, String
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime, timezone, timedelta
import uuid
from sqlalchemy.types import Text, JSON
import sqlalchemy
from enum import Enum
import string
import random

def generate_random_hex_secret(length=6):
    """
    Generate a random hexadecimal string of the specified length.
    
    :param length: Length of the hex string (default is 16).
    :return: Random hex string.
    """
    hex_characters = string.hexdigits.lower()[:6]  # '0123456789abcdef'
    return ''.join(random.choice(hex_characters) for _ in range(length))

class User(SQLModel, table=True):
    id: int = Field(index=True, primary_key=True)
    wallet: str = Field(unique=True)
    points: float = Field(default=1000.0)
    referral_id: str = Field(default_factory=generate_random_hex_secret, unique=True)
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