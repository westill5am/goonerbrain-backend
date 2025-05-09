from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from scrapers import scrape_all_sites

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend on different domain
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/search")
async def search(q: str = Query(...)):
    results = scrape_all_sites(q)
    return results
