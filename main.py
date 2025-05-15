from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from scrapers.scrape_all_sites import scrape_all_sites

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def serve_frontend(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

ILLEGAL_TERMS = [
    "cp", "child", "kids", "preteen", "underage", "minor",
    "lolita", "pedo", "beastiality", "zoophilia", "dog", "horse", "animal",
    "rape", "snuff", "incest", "torture"
]

@app.get("/search")
def search(query: str, mode: str = "straight", page: int = 1):
    normalized = query.lower()
    for term in ILLEGAL_TERMS:
        if term in normalized:
            return {"results": [], "error": "Search term not allowed."}
    results = scrape_all_sites(query, mode, page)
    return {"results": results}
    
@app.get("/tos", response_class=HTMLResponse)
def tos_page(request: Request):
    return templates.TemplateResponse("tos.html", {"request": request})
