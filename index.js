const express = require('express');
const axios = require('axios');
const cheerio = require('cheerio');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 8080;

app.use(cors());

const bannedTerms = ["loli", "rape", "child", "pedo", "incest", "cp", "underage"];

app.get('/search', async (req, res) => {
  const query = req.query.q?.toLowerCase().trim() || "";

  if (!query) {
    return res.status(400).json({ error: "Missing search query." });
  }

  if (bannedTerms.some(term => query.includes(term))) {
    return res.status(403).json({ error: "Search term is blocked." });
  }

  try {
    const [ph, sb] = await Promise.all([
      scrapePornhub(query),
      scrapeSpankBang(query)
    ]);

    const merged = [...ph, ...sb].slice(0, 20); // Limit to 20 results
    res.json({ results: merged });
  } catch (err) {
    console.error("Scraping failed:", err.message);
    res.status(500).json({ error: "Failed to fetch results." });
  }
});

app.listen(PORT, () => {
  console.log(`✅ GoonerBrain API running on port ${PORT}`);
});


// 🔧 Pornhub Scraper
async function scrapePornhub(query) {
  const results = [];
  const res = await axios.get(`https://www.pornhub.com/video/search?search=${encodeURIComponent(query)}`);
  const $ = cheerio.load(res.data);

  $('.pcVideoListItem').each((i, el) => {
    const title = $(el).find('.title a').text().trim();
    const url = 'https://www.pornhub.com' + $(el).find('.title a').attr('href');
    const duration = $(el).find('.duration').text().trim();
    if (title && url) {
      results.push({ title, url, duration, source: "Pornhub" });
    }
  });

  return results;
}


// 🔧 SpankBang Scraper
async function scrapeSpankBang(query) {
  const results = [];
  const res = await axios.get(`https://spankbang.party/s/${encodeURIComponent(query)}`);
  const $ = cheerio.load(res.data);

  $('a.video').each((i, el) => {
    const title = $(el).find('.title').text().trim();
    const url = 'https://spankbang.party' + $(el).attr('href');
    const duration = $(el).find('.duration').text().trim();
    if (title && url) {
      results.push({ title, url, duration, source: "SpankBang" });
    }
  });

  return results;
}
