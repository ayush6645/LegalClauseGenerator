# main.py

from fastapi import FastAPI
from backend.routes import generate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Legal Clause Generator")

# Add middleware after app creation
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend URL for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   

# Include your routers
app.include_router(generate.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Legal Clause Generator API"}