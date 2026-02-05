from fastapi import FastAPI
from pydantic import BaseModel
from agents.planner import Planner
from agents.executor import Executor
from agents.verifier import Verifier

app = FastAPI(title="AI Ops Assistant")

planner = Planner()
executor = Executor()
verifier = Verifier()

class QueryRequest(BaseModel):
    task: str

@app.post("/query")
def process_query(request: QueryRequest):
    plan = planner.create_plan(request.task)
    results = executor.execute(plan)
    final = verifier.verify(request.task, results)
    return final
