const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function fapvid(query) {
  const url = `https://www.fapvid.com/search/videos/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.video').each((i, el) => {
      const title = $(el).find('.title').text().trim();
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://www.fapvid.com' + href,
          duration,
          source: "FapVid"
        });
      }
    });
  } catch (err) {
    console.error("fapvid error:", err.message);
  }

  return results;
};