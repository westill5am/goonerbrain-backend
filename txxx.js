const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function txxx(query) {
  const url = `https://www.txxx.com/search/${encodeURIComponent(query)}/`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('div.video-box').each((i, el) => {
      const title = $(el).find('.title a').text().trim();
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://www.txxx.com' + href,
          duration,
          source: "TXXX"
        });
      }
    });
  } catch (err) {
    console.error("txxx error:", err.message);
  }

  return results;
};
