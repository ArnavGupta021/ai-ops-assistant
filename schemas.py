from pydantic import BaseModel
from typing import List, Dict, Any

class Step(BaseModel):
    tool: str
    parameters: Dict[str, Any]

class Plan(BaseModel):
    steps: List[Step]

class QueryRequest(BaseModel):
    task: str

class QueryResponse(BaseModel):
    summary: str
    details: Dict[str, Any]
