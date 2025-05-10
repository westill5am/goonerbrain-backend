
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio

# Import all real scraper modules
from scrapers import (
    pornhub, tube8, xvideos, spankbang, youporn, eporner, motherless, redgifs,
    bravotube, beeg, txxx, xhamster, hqporner, xnxx, pornhat, sexvids, hclips,
    porndig, yespornplease, porndoe, spankwire, femjoy, javhd
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
async def search(query: str):
    scrapers = [
        pornhub.scrape_pornhub,
        tube8.scrape_tube8,
        xvideos.scrape_xvideos,
        spankbang.scrape_spankbang,
        youporn.scrape_youporn,
        eporner.scrape_eporner,
        motherless.scrape_motherless,
        redgifs.scrape_redgifs,
        bravotube.scrape_bravotube,
        beeg.scrape_beeg,
        txxx.scrape_txxx,
        xhamster.scrape_xhamster,
        hqporner.scrape_hqporner,
        xnxx.scrape_xnxx,
        pornhat.scrape_pornhat,
        sexvids.scrape_sexvids,
        hclips.scrape_hclips,
        porndig.scrape_porndig,
        yespornplease.scrape_yespornplease,
        porndoe.scrape_porndoe,
        spankwire.scrape_spankwire,
        femjoy.scrape_femjoy,
        javhd.scrape_javhd,
    ]

    tasks = [asyncio.to_thread(scraper, query) for scraper in scrapers]
    results_nested = await asyncio.gather(*tasks)
    results = [item for sublist in results_nested for item in sublist]

    return results
