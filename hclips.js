const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function hclips(query) {
  const url = `https://www.hclips.com/search/${encodeURIComponent(query)}/`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.thumb').each((i, el) => {
      const title = $(el).find('.title').text().trim();
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://www.hclips.com' + href,
          duration,
          source: "HClips"
        });
      }
    });
  } catch (err) {
    console.error("hclips error:", err.message);
  }

  return results;
};