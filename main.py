from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import os

app = FastAPI()

# Essential health check endpoint
@app.get("/", tags=["health"])
def root():
    return JSONResponse(
        content={"status": "active", "service": "Casting Couch API"},
        status_code=200
    )

# Add your actual search endpoint
@app.get("/search")
async def search_japanese_uncensored(query: str):
    # Implement your search logic here
    return {"query": query, "results": []}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
