from fastapi import FastAPI
from database import engine, get_db
from contextlib import asynccontextmanager
from models import create_db_and_tables
from fastapi import Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse, RedirectResponse
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
from sqladmin import Admin, ModelView
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from routers import airdrop

class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request):
        form = await request.form()
        username, password = form["username"], form["password"]
        
        if username =='admin' and password == 'password':

        
            request.session.update({"token": "UUID"})

        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        # Check the token in depth
        return True





@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup
    print("db created ")
    create_db_and_tables()
    print("db updated")
    yield  # Your application runs during this yield

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins          # Origins allowed to access your app
    allow_credentials=True,          # Allow cookies
    allow_methods=["*"],             # Allow all HTTP methods
    allow_headers=["*"],             # Allow all headers
)


authentication_backend = AdminAuth(secret_key="88")
admin = Admin(app=app, engine=engine, authentication_backend=authentication_backend)

app.include_router(airdrop.router)



"""app.include_router(auth.router)
app.include_router(admins.router)
app.include_router(users.router)
app.include_router(header.router)
app.include_router(lecture.router)
app.include_router(pq.router)"""





"""class UserAdmin(ModelView, model=User):
    column_list = "__all__"
"""






#admin.add_view(ModelView(Todos))
"""admin.add_view(UserAdmin)

admin.add_view(LevelAdmin)
admin.add_view(OTPAdmin)
admin.add_view(ActivationPinAdmin)
admin.add_view(HeaderImageAdmin)
admin.add_view(RecapAdmin)
admin.add_view(BigNewsAdmin)
admin.add_view(CourseAdmin)
admin.add_view(TopicAdmin)
admin.add_view(QuestionAdmin)
admin.add_view(UserActivationAdmin)"""

