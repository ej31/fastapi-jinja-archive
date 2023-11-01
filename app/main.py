from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.ctrl import case_default, case_if, case_for, case_extends, case_macro, case_include, case_others

app = FastAPI()
app.mount("/static", StaticFiles(directory="resources/static"), name="static_func")
app.include_router(case_default.router)
app.include_router(case_if.router)
app.include_router(case_for.router)
app.include_router(case_extends.router)
app.include_router(case_include.router)
app.include_router(case_others.router)
app.include_router(case_macro.router)
