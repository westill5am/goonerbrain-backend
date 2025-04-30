const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function pornerbros(query) {
  const url = `https://www.pornerbros.com/search/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.list-videos .item').each((i, el) => {
      const title = $(el).find('.title').text().trim();
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://www.pornerbros.com' + href,
          duration,
          source: "PornerBros"
        });
      }
    });
  } catch (err) {
    console.error("pornerbros error:", err.message);
  }

  return results;
};