from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_checker():
    return { "status": "up"}