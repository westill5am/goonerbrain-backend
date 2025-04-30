const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function porndude(query) {
  const url = `https://www.porndude.com/search/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.card-title').each((i, el) => {
      const title = $(el).text().trim();
      const href = $(el).closest('a').attr('href');

      if (title && href) {
        results.push({
          title,
          url: href,
          duration: null,
          source: "PornDude"
        });
      }
    });
  } catch (err) {
    console.error("porndude error:", err.message);
  }

  return results;
};