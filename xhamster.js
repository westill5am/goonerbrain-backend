const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function xhamster(query) {
  const url = `https://xhamster.com/search/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('article.video-thumb').each((i, el) => {
      const title = $(el).find('a.video-thumb__title-link').text().trim();
      const href = $(el).find('a.video-thumb__title-link').attr('href');
      const duration = $(el).find('.video-thumb__duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://xhamster.com' + href,
          duration,
          source: "xHamster"
        });
      }
    });
  } catch (err) {
    console.error("xhamster error:", err.message);
  }

  return results;
};