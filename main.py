from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import scraper

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "OK", "message": "Backend is running!"}

@app.get("/search")
async def search(query: str = Query(..., min_length=1)):
    try:
        results = scraper.search_sites(query)
        return JSONResponse(content={"results": results})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
