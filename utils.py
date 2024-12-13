from fastapi import Depends
from sqlmodel import Session
from typing import Annotated
from database import get_db
db_dependency = Annotated[Session, Depends(get_db)]