const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function beeg(query) {
  const url = `https://beeg.com/search?q=${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('article').each((i, el) => {
      const title = $(el).find('.video-title').text().trim();
      const href = $(el).find('a').attr('href');

      if (title && href) {
        results.push({
          title,
          url: 'https://beeg.com' + href,
          duration: null,
          source: "Beeg"
        });
      }
    });
  } catch (err) {
    console.error("beeg error:", err.message);
  }

  return results;
};