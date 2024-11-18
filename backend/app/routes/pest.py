from fastapi import APIRouter

router = APIRouter()

@router.post("/detect-pest")
def detect_pest():
    return {"pest": "ExamplePest"}
