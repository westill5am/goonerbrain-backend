const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 8080;

app.use(cors());

const bannedTerms = ["loli", "rape", "child", "cp", "underage", "pedo", "incest"];
const SCRAPER_DIR = path.join(__dirname, 'scrapers');

// Load all scraper modules
const scrapers = fs.readdirSync(SCRAPER_DIR)
  .filter(file => file.endsWith('.js'))
  .map(file => require(path.join(SCRAPER_DIR, file)));

app.get('/search', async (req, res) => {
  const query = req.query.q?.toLowerCase().trim() || "";

  if (!query) return res.status(400).json({ error: "Missing search term." });
  if (bannedTerms.some(term => query.includes(term))) {
    return res.status(403).json({ error: "Search term is blocked." });
  }

  try {
    const tasks = scrapers.map(scraper => scraper(query));
    const all = await Promise.allSettled(tasks);

    const results = all
      .filter(r => r.status === 'fulfilled')
      .flatMap(r => r.value)
      .filter((v, i, self) =>
        v && v.url && self.findIndex(x => x.url === v.url) === i
      );

    res.json({ results: results.slice(0, 40) });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Search failed." });
  }
});

app.listen(PORT, () => {
  console.log(`✅ GoonerBrain backend running on port ${PORT}`);
});
