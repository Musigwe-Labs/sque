from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Request, status
from typing import Annotated
from utils import db_dependency
from fastapi.templating import Jinja2Templates




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


@router.get("/h", status_code=status.HTTP_200_OK)
async def read(id: str):
    return id