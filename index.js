const express = require('express');
const app = express();
const cors = require('cors');
const spankbang = require('./scrapers/spankbang.js');

app.use(cors());
app.use(express.static(__dirname));

app.get('/api/search', async (req, res) => {
  const query = req.query.q?.toLowerCase()?.trim();
  if (!query) return res.status(400).json({ error: 'Missing query' });

  try {
    const results = await spankbang(query);
    console.log(`🔎 Search "${query}" returned ${results.length} result(s)`);
    res.json(results);
  } catch (err) {
    console.error('❌ Search error:', err.message);
    res.status(500).json({ error: 'Internal error' });
  }
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`✅ Server listening on port ${PORT}`);
});
