const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function tnaflix(query) {
  const url = `https://www.tnaflix.com/search.php?search=${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.video').each((i, el) => {
      const title = $(el).find('.title').text().trim();
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://www.tnaflix.com' + href,
          duration,
          source: "TNAFlix"
        });
      }
    });
  } catch (err) {
    console.error("tnaflix error:", err.message);
  }

  return results;
};