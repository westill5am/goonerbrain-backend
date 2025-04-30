const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function porndig(query) {
  const url = `https://www.porndig.com/search/videos/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.thumbBlock').each((i, el) => {
      const title = $(el).find('.title').text().trim();
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://www.porndig.com' + href,
          duration,
          source: "PornDig"
        });
      }
    });
  } catch (err) {
    console.error("porndig error:", err.message);
  }

  return results;
};