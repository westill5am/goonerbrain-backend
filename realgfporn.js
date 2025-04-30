const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function realgfporn(query) {
  const url = `https://realgfporn.com/search/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.vid-box').each((i, el) => {
      const title = $(el).find('.title a').text().trim();
      const href = $(el).find('.title a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://realgfporn.com' + href,
          duration,
          source: "RealGFPorn"
        });
      }
    });
  } catch (err) {
    console.error("realgfporn error:", err.message);
  }

  return results;
};