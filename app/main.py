from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.ctrl.base import base_router
from app.models.user import User

app = FastAPI()
app.mount("/static", StaticFiles(directory="resources/static"), name="static_func")
app.include_router(base_router)

templates = Jinja2Templates(directory="resources/template")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{path}")
async def rootV2(path):
    return {"message": "Hello World", "path": path}


@app.get("/item/{item_id}", response_class=HTMLResponse)
async def read_item(request: Request, item_id: str):
    return templates.TemplateResponse(
        name="item.jinja",
        context={
            "request": request,
            "item_id": item_id}
    )

