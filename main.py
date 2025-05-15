# main.py

import os
from pymongo import MongoClient
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# ---- Load env and MongoDB
load_dotenv()
MONGO_URI = os.environ["MONGO_URI"]

client = MongoClient(MONGO_URI)
db = client["vgowitch"]
col = db["keywords"]    # For autocomplete keywords
cache = db["cache"]     # For cached search results

# ---- App Setup
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ---- 18+ / DMCA ILLEGAL TERMS (safety block)
ILLEGAL_TERMS = [
    "cp", "child", "kids", "preteen", "underage", "minor",
    "lolita", "pedo", "beastiality", "zoophilia", "dog", "horse", "animal",
    "rape", "snuff", "incest", "torture"
]

def is_illegal(query):
    normalized = query.lower()
    return any(term in normalized for term in ILLEGAL_TERMS)

# ---- Home: serves your main frontend page
@app.get("/", response_class=HTMLResponse)
def serve_frontend(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ---- Terms of Service Page
@app.get("/tos", response_class=HTMLResponse)
def tos_page(request: Request):
    return templates.TemplateResponse("tos.html", {"request": request})

# ---- Autocomplete API (instant suggestions)
@app.get("/autocomplete")
def autocomplete(term: str):
    suggestions = list(col.find(
        {"keyword": {"$regex": f"^{term}", "$options": "i"}},
        {"_id": 0, "keyword": 1}
    ).limit(20))
    return {"suggestions": [s['keyword'] for s in suggestions]}

# ---- Trending Tags Endpoint (static, can make dynamic)
@app.get("/trending")
def trending():
    tags = [
        "milf", "ebony", "latina", "stepmom", "public", "anal", "amateur", "femboy",
        "anime", "bbc", "big tits", "creampie", "lesbian", "group", "blowjob",
        "tranny", "gay", "sissy", "mature", "hentai"
    ]
    return {"tags": tags}

# ---- Search Endpoint (cache-then-scrape)
@app.get("/search")
def search(query: str, mode: str = "straight", page: int = 1):
    if is_illegal(query):
        return JSONResponse({"results": [], "error": "Search term not allowed."}, status_code=403)
    cache_key = f"{query.lower()}_{mode}_{page}"
    cached = cache.find_one({"_id": cache_key})
    if cached:
        return {"results": cached["results"]}
    from scrapers.scrape_all_sites import scrape_all_sites
    results = scrape_all_sites(query, mode, page)
    cache.insert_one({"_id": cache_key, "results": results})
    return {"results": results}

# ---- Manual cache force/refresh (optional, admin only)
@app.get("/search_new")
def search_new(query: str, mode: str = "straight", page: int = 1):
    if is_illegal(query):
        return JSONResponse({"results": [], "error": "Search term not allowed."}, status_code=403)
    from scrapers.scrape_all_sites import scrape_all_sites
    results = scrape_all_sites(query, mode, page)
    cache_key = f"{query.lower()}_{mode}_{page}"
    cache.update_one({"_id": cache_key}, {"$set": {"results": results}}, upsert=True)
    return {"results": results}

# ---- Health check endpoint
@app.get("/ping")
def ping():
    return {"status": "ok"}
