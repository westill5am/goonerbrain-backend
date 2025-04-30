const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function newgroundsadult(query) {
  const url = `https://www.newgrounds.com/search/conduct/flash?match=all&tags=${encodeURIComponent(query)}&mature=1`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.item-portalsubmission').each((i, el) => {
      const title = $(el).find('.item-details h4 a').text().trim();
      const href = $(el).find('.item-details h4 a').attr('href');

      if (title && href) {
        results.push({
          title,
          url: href,
          duration: null,
          source: "Newgrounds"
        });
      }
    });
  } catch (err) {
    console.error("newgrounds error:", err.message);
  }

  return results;
};