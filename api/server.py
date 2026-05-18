"""AQI API Server - FastAPI interface for external access."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="AQI - Artificial Quranic Intelligence",
    description="API for the Divine AI Suite",
    version="0.2.0",
)

pipeline = None


class QueryRequest(BaseModel):
    query: str
    frameworks: list[str] | None = None


class QueryResponse(BaseModel):
    query: str
    results: dict
    summary: str


@app.on_event("startup")
async def startup():
    global pipeline
    from integration.pipeline import AQIPipeline
    pipeline = AQIPipeline()
    pipeline.initialize()


@app.get("/")
async def root():
    return {
        "name": "AQI - Artificial Quranic Intelligence",
        "version": "0.2.0",
        "frameworks": ["TES", "NBCD", "DNO", "EPM", "PDI-GPT"],
    }


@app.get("/health")
async def health():
    return {"status": "healthy", "pipeline_initialized": pipeline is not None}


@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    if pipeline is None:
        raise HTTPException(status_code=503, detail="Pipeline not initialized")

    results = pipeline.process(request.query)
    summary = pipeline.get_summary(results)

    return QueryResponse(
        query=request.query,
        results=results,
        summary=summary,
    )


@app.get("/frameworks")
async def list_frameworks():
    return {
        "TES": "Theological Embedding Space",
        "NBCD": "Nass-Based Causal Discovery",
        "DNO": "Divine Names Ontology",
        "EPM": "Eschatological Predictive Modeling",
        "PDI-GPT": "Prophetic Dream Interpreter",
    }
