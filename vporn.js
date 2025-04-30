const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function vporn(query) {
  const url = `https://www.vporn.com/?k=${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.thumb-block').each((i, el) => {
      const title = $(el).find('a').attr('title');
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title: title.trim(),
          url: 'https://www.vporn.com' + href,
          duration,
          source: "VPorn"
        });
      }
    });
  } catch (err) {
    console.error("vporn error:", err.message);
  }

  return results;
};