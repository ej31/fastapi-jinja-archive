from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter(prefix="/base")
templates = Jinja2Templates(directory="resources/template")


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        name="sample.html",
        context={
            "request": request
        }
    )
    # return {"message": "Hello World", "path": path}


@router.get("/hello/{path}")
async def rootV2(path):
    return {"message": "Hello World rootV2!", "path": path}


@router.get("/item/{item_id}", response_class=HTMLResponse)
async def read_item(request: Request, item_id: str):
    #
    #
    # 데이터베이스 처리하는 코드 어쩌구...
    # 저쩌구...
    #
    #

    return templates.TemplateResponse(
        name="default/item.jinja",
        context={
            "request": request,
            "item_id": item_id
        }
    )
