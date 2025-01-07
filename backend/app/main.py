# main.py
from fastapi import FastAPI
from app.routes import router  # Import the router from the routes module

# Create the FastAPI app
app = FastAPI()

# Include the router for the endpoints
app.include_router(router)



