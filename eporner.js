const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function eporner(query) {
  const url = `https://www.eporner.com/search/?q=${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.mb').each((i, el) => {
      const title = $(el).find('a.title').text().trim();
      const href = $(el).find('a.title').attr('href');
      const duration = $(el).find('.time').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://www.eporner.com' + href,
          duration,
          source: "Eporner"
        });
      }
    });
  } catch (err) {
    console.error("eporner error:", err.message);
  }

  return results;
};
