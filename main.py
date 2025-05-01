# main.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from spankbang import scrape_spankbang

app = FastAPI()

# Allow frontend requests from anywhere
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/search")
async def search(q: str = Query(..., min_length=1)):
    try:
        results = await scrape_spankbang(q)
        return results
    except Exception as e:
        return {"error": str(e)}
