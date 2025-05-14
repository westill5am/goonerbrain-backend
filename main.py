from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn

# 🔥 Import your scraper logic (adjust this if needed)
from scrapers import scrape_sites  # or whatever your actual module is

app = FastAPI()

# ✅ CORS Middleware Fix
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://goonerbrain.com"],  # only your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Main search route
@app.get("/search")
async def search(query: str = Query(..., min_length=1)):
    try:
        results = scrape_sites(query)
        return {"results": results}
    except Exception as e:
        return {"error": str(e)}

# 🧪 Local testing (if needed)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
