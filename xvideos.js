const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function xvideos(query) {
  const url = `https://www.xvideos.com/?k=${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.thumb-block').each((i, el) => {
      const title = $(el).find('.title a').text().trim();
      const href = $(el).find('.title a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://www.xvideos.com' + href,
          duration,
          source: "XVideos"
        });
      }
    });
  } catch (err) {
    console.error("xvideos error:", err.message);
  }

  return results;
};