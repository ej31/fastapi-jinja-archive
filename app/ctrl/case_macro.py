from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter(prefix="/macro")
templates = Jinja2Templates(directory="resources/template")


@router.get("/case1", response_class=HTMLResponse)
def macro_sample_1(request: Request):
    return templates.TemplateResponse(
        name='macro/index.jinja',
        context={'request': request}
    )


@router.get("/case2", response_class=HTMLResponse)
def macro_sample_2(request: Request):
    return templates.TemplateResponse(
        name='macro/somepage.jinja',
        context={'request': request}
    )
