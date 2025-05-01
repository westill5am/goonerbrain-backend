from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Enable CORS so frontend can call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production: use your frontend URL only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root test route
@app.get("/")
def root():
    return {"message": "GoonerBrain API is live."}

# ✅ Working search route
@app.get("/search")
async def search(q: str = Query(...)):
    return {
        "results": [
            {
                "title": f"Fake result for '{q}'",
                "thumb": "https://placehold.co/400x225?text=Preview",
                "link": "https://example.com/fake"
            }
        ]
    }
