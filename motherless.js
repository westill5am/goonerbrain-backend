const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function motherless(query) {
  const url = `https://motherless.com/videos?q=${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('div.video-thumb').each((i, el) => {
      const title = $(el).find('.video-title').text().trim();
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://motherless.com' + href,
          duration,
          source: "Motherless"
        });
      }
    });
  } catch (err) {
    console.error("motherless error:", err.message);
  }

  return results;
};