const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function nudogram(query) {
  const url = `https://nudogram.com/search/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.thumb').each((i, el) => {
      const title = $(el).find('img').attr('alt');
      const href = $(el).find('a').attr('href');

      if (title && href) {
        results.push({
          title: title.trim(),
          url: 'https://nudogram.com' + href,
          duration: null,
          source: "Nudogram"
        });
      }
    });
  } catch (err) {
    console.error("nudogram error:", err.message);
  }

  return results;
};