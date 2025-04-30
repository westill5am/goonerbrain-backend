const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function redtube(query) {
  const url = `https://www.redtube.com/?search=${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.video').each((i, el) => {
      const title = $(el).find('.video-title').text().trim();
      const href = $(el).find('a').attr('href');
      const thumb = $(el).find('img').attr('src');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://www.redtube.com' + href,
          duration,
          source: "Redtube"
        });
      }
    });
  } catch (err) {
    console.error("redtube error:", err.message);
  }

  return results;
};
