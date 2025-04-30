const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function fuq(query) {
  const url = `https://fuq.com/search/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.thumb').each((i, el) => {
      const title = $(el).find('a').attr('title');
      const href = $(el).find('a').attr('href');

      if (title && href) {
        results.push({
          title: title.trim(),
          url: 'https://fuq.com' + href,
          duration: null,
          source: "Fuq"
        });
      }
    });
  } catch (err) {
    console.error("fuq error:", err.message);
  }

  return results;
};