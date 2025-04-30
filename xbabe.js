const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function xbabe(query) {
  const url = `https://xbabe.com/search/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.video-block').each((i, el) => {
      const title = $(el).find('.video-title').text().trim();
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://xbabe.com' + href,
          duration,
          source: "XBabe"
        });
      }
    });
  } catch (err) {
    console.error("xbabe error:", err.message);
  }

  return results;
};