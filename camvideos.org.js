const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function camvideos(query) {
  const url = `https://camvideos.org/?s=${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('article').each((i, el) => {
      const title = $(el).find('h2 a').text().trim();
      const href = $(el).find('h2 a').attr('href');

      if (title && href) {
        results.push({
          title,
          url: href,
          duration: null,
          source: "CamVideos"
        });
      }
    });
  } catch (err) {
    console.error("camvideos error:", err.message);
  }

  return results;
};