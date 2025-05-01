from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI(title="Casting Couch API", version="1.0.0")

# Essential for Render health checks
@app.get("/", include_in_schema=False)
def health_check():
    return {"status": "active"}

# Add your actual endpoints here
@app.get("/search")
async def search_query(q: str):
    # Your search logic here
    return {"results": []}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
