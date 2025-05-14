from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from scraper import scrape_all_sites

app = FastAPI()

# Allow frontend access (local + deployed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://goonerbrain.com", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/search")
async def search(query: str = Query(...)):
    print(f"🔍 Received query: {query}")
    results = scrape_all_sites(query)
    print(f"📦 Returning {len(results)} results")
    return {"results": results}
