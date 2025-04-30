const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function tubedupe(query) {
  const url = `https://www.tubedupe.com/search/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.thumb').each((i, el) => {
      const title = $(el).find('.title a').text().trim();
      const href = $(el).find('.title a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://www.tubedupe.com' + href,
          duration,
          source: "TubeDupe"
        });
      }
    });
  } catch (err) {
    console.error("tubedupe error:", err.message);
  }

  return results;
};