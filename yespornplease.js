const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function yespornplease(query) {
  const url = `https://yespornplease.to/?s=${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.post').each((i, el) => {
      const title = $(el).find('h2 a').text().trim();
      const href = $(el).find('h2 a').attr('href');

      if (title && href) {
        results.push({
          title,
          url: href,
          duration: null,
          source: "YesPornPlease"
        });
      }
    });
  } catch (err) {
    console.error("yespornplease error:", err.message);
  }

  return results;
};