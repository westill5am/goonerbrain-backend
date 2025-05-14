from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

# CORS fix for frontend/backend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://goonerbrain.com"],
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
    return {
        "results": [
            {
                "title": f"🔥 Dummy video result for '{query}'",
                "url": "https://example.com",
                "preview": "https://via.placeholder.com/300x160.png?text=Preview",
                "source": "test"
            }
        ]
    }
