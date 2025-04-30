const express = require('express');
const cors = require('cors');
const axios = require('axios');
const cheerio = require('cheerio');

const app = express();
const PORT = process.env.PORT || 8080;

app.use(cors());

const bannedTerms = ["loli", "rape", "child", "pedo", "incest", "cp"];

app.get('/search', async (req, res) => {
  const query = req.query.q?.toLowerCase() || "";

  if (bannedTerms.some(term => query.includes(term))) {
    return res.status(403).json({ error: "Search term is blocked." });
  }

  try {
    const [phResults, xvResults] = await Promise.all([
      scrapePornhub(query),
      scrapeXVideos(query)
    ]);

    const combinedResults = [...phResults, ...xvResults];
    res.json({ results: combinedResults });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Search failed." });
  }
});

app.listen(PORT, () => console.log(`🧠 GoonerBrain API running on port ${PORT}`));

// Helper functions
async function scrapePornhub(query) {
  const url = `https://www.pornhub.com/video/search?search=${encodeURIComponent(query)}`;
  const { data } = await axios.get(url);
  const $ = cheerio.load(data);
  const results = [];

  $('.videoPreviewBg').each((i, el) => {
    const title = $(el).attr('data-title');
    const videoUrl = 'https://www.pornhub.com' + $(el).parent().attr('href');
    const duration = $(el).find('.duration').text().trim();
    if (title && videoUrl) {
      results.push({
        title,
        url: videoUrl,
        duration,
        source: "Pornhub"
      });
    }
  });

  return results;
}

async function scrapeXVideos(query) {
  const url = `https://www.xvideos.com/?k=${encodeURIComponent(query)}`;
  const { data } = await axios.get(url);
  const $ = cheerio.load(data);
  const results = [];

  $('.thumb-block').each((i, el) => {
    const title = $(el).find('.title a').text().trim();
    const videoUrl = 'https://www.xvideos.com' + $(el).find('.title a').attr('href');
    const duration = $(el).find('.duration').text().trim();
    if (title && videoUrl) {
      results.push({
        title,
        url: videoUrl,
        duration,
        source: "XVideos"
      });
    }
  });

  return results;
}
