const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function nuditybay(query) {
  const url = `https://nuditybay.com/?s=${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.post-title a').each((i, el) => {
      const title = $(el).text().trim();
      const href = $(el).attr('href');

      if (title && href) {
        results.push({
          title,
          url: href,
          duration: null,
          source: "NudityBay"
        });
      }
    });
  } catch (err) {
    console.error("nuditybay error:", err.message);
  }

  return results;
};