from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import os

# ✅ Adjust to your real scrape module
from scraper import scrape_all_sites

app = FastAPI()

# ✅ CORS setup to allow frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://goonerbrain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Jinja2 template loader
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/search")
async def search(query: str = Query(..., min_length=1)):
    try:
        results = scrape_all_sites(query)
        print(f"🔍 Query: '{query}' — Returned {len(results)} results")
        return {"results": results}
    except Exception as e:
        print(f"❌ Scraper error: {str(e)}")
        return {
            "results": [
                {
                    "title": f"Fake video for '{query}'",
                    "url": "https://example.com",
                    "preview": "https://via.placeholder.com/300x160?text=Preview",
                    "source": "fallback"
                }
            ],
            "error": str(e)
        }
