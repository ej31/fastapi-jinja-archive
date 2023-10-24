from fastapi import APIRouter

from app.ctrl import case_default, case_if, case_for

base_router = APIRouter()
base_router.include_router(case_default.router)
base_router.include_router(case_if.router)
base_router.include_router(case_for.router)
