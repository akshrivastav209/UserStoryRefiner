# app/routes.py
from fastapi import APIRouter
from .services import get_data  # Import the function from services.py

router = APIRouter()

@router.get("/data")  # Define the route at "/data"
async def read_data():
    return get_data()  # Return the data from services.py
