from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncio
from scraper import scrape_sites

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, query: str = "example"):
    results = await scrape_sites(query)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "query": query,
        "results": results
    })
