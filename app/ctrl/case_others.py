from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter(prefix="/ohters")
templates = Jinja2Templates(directory="resources/template")


@router.get("/set-1", response_class=HTMLResponse)
def sample_set(request: Request):
    return templates.TemplateResponse(
        name='others/set-case1.jinja',
        context={'request': request}
    )


@router.get("/set-2", response_class=HTMLResponse)
def sample_set(request: Request):
    return templates.TemplateResponse(
        name='others/set-case1.jinja',
        context={'request': request}
    )


@router.get("/filter", response_class=HTMLResponse)
def sample_inline(request: Request):
    return templates.TemplateResponse(
        name='others/filter.jinja',
        context={
            'request': request,
            'name': 'Michael Jackson',
            'price': 1_000_000_000.191919
        }
    )

