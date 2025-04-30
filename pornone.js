const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function pornone(query) {
  const url = `https://www.pornone.com/search/${encodeURIComponent(query)}/`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.item-video').each((i, el) => {
      const title = $(el).find('.video-title').text().trim();
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://www.pornone.com' + href,
          duration,
          source: "PornOne"
        });
      }
    });
  } catch (err) {
    console.error("pornone error:", err.message);
  }

  return results;
};