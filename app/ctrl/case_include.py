from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter(prefix="/include")
templates = Jinja2Templates(directory="resources/template")


@router.get("/", response_class=HTMLResponse)
def macro_sample_1(request: Request):
    return templates.TemplateResponse(
        name='include/main.jinja',
        context={'request': request}
    )
