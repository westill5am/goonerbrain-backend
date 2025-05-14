from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from scrapers.scrape_all_sites import scrape_all_sites

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def serve_frontend(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/search")
def search(query: str, mode: str = "straight", page: int = 1):
    results = scrape_all_sites(query, mode, page)
    return {"results": results}
