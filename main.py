from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scrapers import (
    hqporner, tube8, xvideos, spankbang, motherless,
    youporn, bravotube, eporner, beeg, xhamster, fux
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"message": "GoonerBrain Backend is online"}

@app.get("/search")
def search(query: str):
    results = []
    results += hqporner.scrape_hqporner(query)
    results += tube8.scrape_tube8(query)
    results += xvideos.scrape_xvideos(query)
    results += spankbang.scrape_spankbang(query)
    results += motherless.scrape_motherless(query)
    results += youporn.scrape_youporn(query)
    results += bravotube.scrape_bravotube(query)
    results += eporner.scrape_eporner(query)
    results += beeg.scrape_beeg(query)
    results += xhamster.scrape_xhamster(query)
    results += fux.scrape_fux(query)
    return results
