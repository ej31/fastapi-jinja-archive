from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.models.item import Item
from app.models.user import User

router = APIRouter(prefix="/extends")
templates = Jinja2Templates(directory="resources/template")


@router.get("/", response_class=HTMLResponse)
async def extends_sample(request: Request):
    return templates.TemplateResponse(
        name="extends/page.jinja", context={"request": request}
    )
