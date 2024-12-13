from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Request, status
from typing import Annotated
from utils import db_dependency
from fastapi.templating import Jinja2Templates
from sqlmodel import select
from models import User



router = APIRouter(prefix='',tags=['Home'])

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html")


@router.get("/airdrop/login", response_class=HTMLResponse)
async def airdrop_login(request: Request):
    return templates.TemplateResponse(
        request=request, name="login.html")



@router.get("/dashboard/", response_class=HTMLResponse)
async def dashboard_b(request: Request, wallet_add: str, db: db_dependency):
    statement = select(User).where(User.wallet == wallet_add)
    user = db.exec(statement).first()

    return templates.TemplateResponse(
        request=request, name="dashboard.html", context={"user": user})



@router.get("/h", status_code=status.HTTP_200_OK)
async def read(id: str):
    return id