const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function porncom(query) {
  const url = `https://www.porn.com/videos/search?q=${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.video').each((i, el) => {
      const title = $(el).find('a.title').text().trim();
      const href = $(el).find('a.title').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://www.porn.com' + href,
          duration,
          source: "Porn.com"
        });
      }
    });
  } catch (err) {
    console.error("porn.com error:", err.message);
  }

  return results;
};
