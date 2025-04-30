const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function pichunter(query) {
  const url = `https://www.pichunter.com/search/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.videoBox').each((i, el) => {
      const title = $(el).find('.videoTitle').text().trim();
      const href = $(el).find('a').attr('href');

      if (title && href) {
        results.push({
          title,
          url: 'https://www.pichunter.com' + href,
          duration: null,
          source: "PicHunter"
        });
      }
    });
  } catch (err) {
    console.error("pichunter error:", err.message);
  }

  return results;
};