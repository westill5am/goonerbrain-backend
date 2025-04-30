const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function bangbrosnetwork(query) {
  const url = `https://bangbrosnetwork.com/video/search/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.item').each((i, el) => {
      const title = $(el).find('.title').text().trim();
      const href = $(el).find('a').attr('href');

      if (title && href) {
        results.push({
          title,
          url: 'https://bangbrosnetwork.com' + href,
          duration: null,
          source: "BangBrosNetwork"
        });
      }
    });
  } catch (err) {
    console.error("bangbrosnetwork error:", err.message);
  }

  return results;
};