from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.models.user import User

router = APIRouter(prefix="/if")
templates = Jinja2Templates(directory="resources/template")


@router.get("/user/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    __user = User(name=name, age=20, sex="Male", role="admin")  # 유저가 있다는 전제하에 가짜 유저 생성

    return templates.TemplateResponse(
        name="if/sample-if-case3.jinja",
        context={
            "request": request,
            "user": __user}
    )


@router.get("/user/{name}/role", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    __user = User(name=name, age=20, sex="Male", role="admin")  # 유저가 있다는 전제하에 가짜 유저 생성
    return templates.TemplateResponse(
        name="if/sample-if-case4.jinja",
        context={
            "request": request,
            "user": __user
        }
    )
