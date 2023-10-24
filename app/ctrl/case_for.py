from fastapi import APIRouter
from jinja2.ext import LoopControlExtension
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.models.item import Item

router = APIRouter(prefix="/for")
templates = Jinja2Templates(directory="resources/template", extensions=[LoopControlExtension])


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    __items = [
        Item("선풍기", "White", 100_000),
        Item("책상", "Red", 190_000)
    ]

    return templates.TemplateResponse(
        name="for/sample-case1.jinja",
        context={
            "request": request,
            "items": __items,
        }
    )


@router.get("/with-enum", response_class=HTMLResponse)
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


@router.get("/with-loop", response_class=HTMLResponse)
async def read_item(request: Request):
    __items = [
        Item("선풍기", "White", 100_000),
        Item("책상", "Red", 190_000)
    ]
    return templates.TemplateResponse(
        name="for/sample-case3.jinja",
        context={
            "request": request,
            "items": __items}
    )


@router.get("/with-control", response_class=HTMLResponse)
async def read_item(request: Request):
    __items = [
        Item("선풍기", "White", 100_000),
        Item("책상", "Red", 190_000),
        Item("TV", "Black", 30_000_000),
        Item("냉장고", "Black", 6_000_000, state="skip"),
        Item("세탁기", "Silver", 3_000_000, state="stop")
    ]

    return templates.TemplateResponse(
        name="for/sample-case4.jinja",
        context={
            "request": request,
            "items": __items}
    )
