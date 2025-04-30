const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function proprono(query) {
  const url = `https://proporno.com/search/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.thumb').each((i, el) => {
      const title = $(el).find('a').attr('title');
      const href = $(el).find('a').attr('href');

      if (title && href) {
        results.push({
          title: title.trim(),
          url: 'https://proporno.com' + href,
          duration: null,
          source: "ProPorno"
        });
      }
    });
  } catch (err) {
    console.error("proporno error:", err.message);
  }

  return results;
};