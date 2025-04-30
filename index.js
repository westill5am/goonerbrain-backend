const express = require('express');
const cors = require('cors');
const axios = require('axios');

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
    // This example simulates SpankBang search results.
    const dummyResults = [
      {
        title: `Results for "${query}"`,
        url: `https://spankbang.com/s/${encodeURIComponent(query)}`,
        duration: "10:32",
        source: "SpankBang"
      },
      {
        title: `Another hit: ${query}`,
        url: `https://xvideos.com/?k=${encodeURIComponent(query)}`,
        duration: "7:45",
        source: "XVideos"
      }
    ];

    res.json({ results: dummyResults });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Search failed." });
  }
});

app.listen(PORT, () => console.log(`🧠 GoonerBrain API running on port ${PORT}`));
