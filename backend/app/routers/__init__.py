from fastapi import APIRouter

from .pipeline import router as pipeline_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(pipeline_router)
