from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

# 👉 Updated import: using Gemini handler instead of OpenAI
from backend.services.gemini_handler import generate_legal_clauses

router = APIRouter()

ALLOWED_CLAUSE_TYPES = {"Confidentiality", "Indemnity", "Termination"}

class GenerateRequest(BaseModel):
    prompt: str
    clause_type: str
    context: str = ""

class GenerateResponse(BaseModel):
    suggestions: List[str]

@router.post("/generate", response_model=GenerateResponse)
async def generate_clause(data: GenerateRequest):
    if not data.prompt or not data.clause_type:
        raise HTTPException(status_code=400, detail="Both prompt and clause_type are required.")

    if data.clause_type not in ALLOWED_CLAUSE_TYPES:
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid clause_type. Must be one of: {', '.join(ALLOWED_CLAUSE_TYPES)}"
        )

    try:
        clauses = await generate_legal_clauses(
            prompt=data.prompt,
            clause_type=data.clause_type,
            context=data.context,
            n_suggestions=3
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating clauses: {str(e)}")

    if not clauses:
        raise HTTPException(status_code=500, detail="Failed to generate clauses.")

    return {"suggestions": clauses}
