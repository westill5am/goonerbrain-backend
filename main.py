from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# ✅ Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://goonerbrain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")

@app.get("/search")
async def search(query: str = Query(...)):
    print(f"🔍 Received query: {query}")
    results = [
        {
            "title": f"Test video for '{query}'",
            "url": "https://example.com",
            "preview": "https://via.placeholder.com/300x160?text=Preview",
            "source": "test"
        }
    ]
    print(f"✅ Returning {len(results)} fake result(s)")
    return {"results": results}
