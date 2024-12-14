from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Request, status
from typing import Annotated, Optional
from utils import db_dependency
from fastapi.templating import Jinja2Templates
from sqlmodel import select
from models import User
from fastapi.exceptions import HTTPException



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

    referral_link = f"{request.base_url}airdrop/?ref={user.referral_id}"

    return templates.TemplateResponse(
        request=request, name="dashboard.html", context={"user": user, "ref_link": referral_link})




@router.get("/airdrop/", response_class=HTMLResponse)
async def airdrop_form(request: Request):
    return templates.TemplateResponse(
        request=request, name="squeeairdrop.html")

@router.get("/airdropa/", response_class=HTMLResponse)
async def airdrop_formpost(request: Request, wallet:str, rt_link: str, db: db_dependency,
                           tg_username: str,  ref: str =None):
    
    existing_user_state = select(User).where(User.wallet ==wallet)
    existing_user = db.exec(existing_user_state).first()

    if existing_user:
        return templates.TemplateResponse(
            "error.html",  # Replace with your error page template
            {
                "request": request,
                "error_message": "A User with this Wallet has registered already.",
            },
            status_code=status.HTTP_403_FORBIDDEN,
        )
    
    #Save User
    
    
    new_user = User(wallet=wallet, rt_link=rt_link, tg_username=tg_username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print("ref:", ref)


     #Check and reward the person that refered
    referral_statement = select(User).where(User.referral_id ==ref)
    refered_user = db.exec(referral_statement).first()

    if not refered_user:
        referral_link = f"{request.base_url}airdrop/?ref={new_user.referral_id}"

        return templates.TemplateResponse(
        request=request, name="dashboard.html", context={"user": new_user, "ref_link": referral_link})
        

    refered_user.points += 500

    


    db.add(refered_user)
    db.commit()
    referral_link = f"{request.base_url}airdrop/?ref={new_user.referral_id}"




    return templates.TemplateResponse(
        request=request, name="dashboard.html", context={"user": new_user, "ref_link": referral_link})



@router.get("/h", status_code=status.HTTP_200_OK)
async def read(id: str):
    return id