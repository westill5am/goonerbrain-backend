const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function rule34video(query) {
  const url = `https://rule34video.com/?s=${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.video-title').each((i, el) => {
      const title = $(el).text().trim();
      const href = $(el).closest('a').attr('href');

      if (title && href) {
        results.push({
          title,
          url: href,
          duration: null,
          source: "Rule34Video"
        });
      }
    });
  } catch (err) {
    console.error("rule34video error:", err.message);
  }

  return results;
};