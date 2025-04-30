const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function hotmovs(query) {
  const url = `https://hotmovs.com/?s=${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.video').each((i, el) => {
      const title = $(el).find('.title').text().trim();
      const href = $(el).find('a').attr('href');

      if (title && href) {
        results.push({
          title,
          url: href,
          duration: null,
          source: "HotMovs"
        });
      }
    });
  } catch (err) {
    console.error("hotmovs error:", err.message);
  }

  return results;
};