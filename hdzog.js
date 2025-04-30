const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function hdzog(query) {
  const url = `https://www.hdzog.com/search/${encodeURIComponent(query)}/`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.thumb').each((i, el) => {
      const title = $(el).find('a').attr('title');
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title: title.trim(),
          url: 'https://www.hdzog.com' + href,
          duration,
          source: "HDZog"
        });
      }
    });
  } catch (err) {
    console.error("hdzog error:", err.message);
  }

  return results;
};