from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.models.item import Item
from app.models.user import User

router = APIRouter(prefix="/for")
templates = Jinja2Templates(directory="resources/template")


@router.get("/item", response_class=HTMLResponse)
async def read_item(request: Request):
    __items = [
        Item("선풍기", "White", 100_000),
        Item("책상", "Red", 190_000)
    ]

    return templates.TemplateResponse(
        name="for/sample-case1.jinja",
        context={
            "request": request,
            "items": __items}
    )


@router.get("/item/with-enum", response_class=HTMLResponse)
async def read_item(request: Request):
    __items = [
        Item("선풍기", "White", 100_000),
        Item("책상", "Red", 190_000)
    ]
    return templates.TemplateResponse(
        name="for/sample-case2.jinja",
        context={
            "request": request,
            "items": enumerate(__items)}
    )
