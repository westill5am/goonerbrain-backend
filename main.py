from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from scraper import scrape_all_sites  # adjust if you're using `scrapers/` folder

app = FastAPI()

# CORS: Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://goonerbrain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve template
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/search")
async def search(query: str = Query(..., min_length=1)):
    try:
        results = scrape_all_sites(query)
        return {"results": results}
    except Exception as e:
        return {"results": [], "error": str(e)}
