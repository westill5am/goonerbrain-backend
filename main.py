# main.py
from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from spankbang import scrape_spankbang

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Allow frontend requests from anywhere
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/search")
async def search(q: str = Query(..., min_length=1)):
    try:
        results = await scrape_spankbang(q)
        return results
    except Exception as e:
        return {"error": str(e)}
