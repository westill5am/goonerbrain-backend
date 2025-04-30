const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function fux(query) {
  const url = `https://www.fux.com/videos/search/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.item-video').each((i, el) => {
      const title = $(el).find('.title').text().trim();
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://www.fux.com' + href,
          duration,
          source: "Fux"
        });
      }
    });
  } catch (err) {
    console.error("fux error:", err.message);
  }

  return results;
};