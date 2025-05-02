from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import scraper

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "OK", "message": "Backend is running"}

@app.get("/search")
async def search(query: str = Query(..., min_length=1)):
    print(f"🚨 Search called with query: {query}")
    try:
        results = scraper.search_sites(query)
        print(f"✅ Returning {len(results)} results")
        return JSONResponse(content={"results": results})
    except Exception as e:
        print(f"❌ Error: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
