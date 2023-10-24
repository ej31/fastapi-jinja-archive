from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter(prefix="/base")
templates = Jinja2Templates(directory="resources/template")


@router.get("/hello/{path}")
async def rootV2(path):
    return {"message": "Hello World", "path": path}


@router.get("/item/{item_id}", response_class=HTMLResponse)
async def read_item(request: Request, item_id: str):
    return templates.TemplateResponse(
        name="item.jinja",
        context={
            "request": request,
            "item_id": item_id}
    )
