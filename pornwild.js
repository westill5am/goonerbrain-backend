const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function pornwild(query) {
  const url = `https://www.pornwild.to/search/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.video-title').each((i, el) => {
      const title = $(el).text().trim();
      const href = $(el).closest('a').attr('href');

      if (title && href) {
        results.push({
          title,
          url: 'https://www.pornwild.to' + href,
          duration: null,
          source: "PornWild"
        });
      }
    });
  } catch (err) {
    console.error("pornwild error:", err.message);
  }

  return results;
};