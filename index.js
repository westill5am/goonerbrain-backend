const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
app.use(cors());

const PORT = process.env.PORT || 3000;

// 🔒 Blocked Terms
const bannedTerms = ['rape', 'loli', 'cp', 'child', 'underage'];

app.get('/search', async (req, res) => {
  const query = req.query.q;
  if (!query) return res.status(400).json({ error: 'Missing query' });

  const lowerQuery = query.toLowerCase();
  if (bannedTerms.some(term => lowerQuery.includes(term))) {
    return res.status(403).json({ error: 'Illegal search term blocked' });
  }

  try {
    const results = [];

    // Pornhub (via unofficial endpoint)
    const ph = await axios.get(`https://www.pornhub.com/webmasters/search?search=${encodeURIComponent(query)}`);
    if (ph.data?.videos) {
      ph.data.videos.forEach(video => {
        results.push({
          source: 'Pornhub',
          title: video.title,
          url: video.url,
          duration: video.duration,
          thumb: video.thumb,
        });
      });
    }

    // SpankBang (using open scraping)
    const sb = await axios.get(`https://spankbang.party/api/videos/search?phrase=${encodeURIComponent(query)}&limit=8`);
    if (sb.data?.results) {
      sb.data.results.forEach(video => {
        results.push({
          source: 'SpankBang',
          title: video.title,
          url: `https://spankbang.com${video.url}`,
          duration: video.duration,
          thumb: video.thumb,
        });
      });
    }

    res.json({ results });
  } catch (err) {
    res.status(500).json({ error: 'Error fetching data' });
  }
});

app.listen(PORT, () => {
  console.log(`GoonerBrain API is live on port ${PORT}`);
});
