from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from scraper import scrape_all_sites  # this matches your file

app = FastAPI()

# ✅ CORS Middleware to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://goonerbrain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Main /search endpoint
@app.get("/search")
async def search(query: str = Query(..., min_length=1)):
    try:
        results = scrape_all_sites(query)
        return {"results": results}
    except Exception as e:
        return {"error": str(e)}
