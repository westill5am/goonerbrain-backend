const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function xxxbunker(query) {
  const url = `https://xxxbunker.com/search/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.video-thumb').each((i, el) => {
      const title = $(el).find('a').attr('title');
      const href = $(el).find('a').attr('href');

      if (title && href) {
        results.push({
          title: title.trim(),
          url: 'https://xxxbunker.com' + href,
          duration: null,
          source: "XXXBunker"
        });
      }
    });
  } catch (err) {
    console.error("xxxbunker error:", err.message);
  }

  return results;
};