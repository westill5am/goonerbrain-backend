const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function pornhub(query) {
  const url = `https://www.pornhub.com/video/search?search=${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.videoPreviewBg').each((i, el) => {
      const title = $(el).find('img').attr('alt') || '';
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title: title.trim(),
          url: 'https://www.pornhub.com' + href,
          duration,
          source: "Pornhub"
        });
      }
    });
  } catch (err) {
    console.error("pornhub error:", err.message);
  }

  return results;
};