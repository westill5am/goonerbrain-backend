from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from scraper.scrape_all_sites import scrape_all_sites  # Adjust this path if needed

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/search")
async def search(query: str = Query(...), mode: str = Query("straight")):
    print(f"\n🔍 Query: {query}, Mode: {mode}")
    results = scrape_all_sites(query, mode)
    return {"results": results}
