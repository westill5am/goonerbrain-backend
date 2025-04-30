const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function hqporner(query) {
  const url = `https://hqporner.com/search/${encodeURIComponent(query)}.html`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.list-video').each((i, el) => {
      const title = $(el).find('.title a').text().trim();
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://hqporner.com' + href,
          duration,
          source: "HQPorner"
        });
      }
    });
  } catch (err) {
    console.error("hqporner error:", err.message);
  }

  return results;
};