from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import asyncio

app = FastAPI()

# ✅ CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root test route
@app.get("/")
def read_root():
    return {"message": "GoonerBrain API is running!"}

# ✅ Search endpoint
@app.get("/search")
async def search(q: str = Query(..., description="Your porn search query")):
    # placeholder logic – replace this with your real scraping pool
    return {
        "query": q,
        "results": [
            {
                "title": f"Example result for '{q}'",
                "thumb": "https://example.com/thumb.jpg",
                "link": "https://example.com/video"
            }
        ]
    }
