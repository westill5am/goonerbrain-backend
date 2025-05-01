from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Allow frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production: ["https://goonerbrain.vercel.app"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root endpoint (test if backend works at all)
@app.get("/")
def root():
    return {"message": "GoonerBrain API is running."}

# ✅ Search endpoint that the frontend needs
@app.get("/search")
async def search(q: str = Query(...)):
    if not q:
        return {"results": []}
    
    # Placeholder search logic (add real scraping later)
    return {
        "results": [
            {
                "title": f"Fake video for '{q}'",
                "thumb": "https://placehold.co/400x200?text=Preview",
                "link": "https://example.com/fake"
            }
        ]
    }
