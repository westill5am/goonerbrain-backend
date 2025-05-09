from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from scraper import scrape_sites

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, query: str = None):
    results = await scrape_sites(query) if query else []
    return templates.TemplateResponse("index.html", {
        "request": request,
        "query": query,
        "results": results
    })
