const axios = require('axios');
const cheerio = require('cheerio');
module.exports = async function brazzers(query) {
  const results = [];
  try {
    const url = "https://example.com/search?q=" + encodeURIComponent(query);
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    // TODO: customize selector for brazzers

    $('selector').each((i, el) => {
      const title = $(el).text().trim();
      const href = $(el).attr('href');
      if (title && href) {
        results.push({
          title,
          url: href.startsWith('http') ? href : 'https://example.com' + href,
          duration: '',
          source: "brazzers"
        });
      }
    });
  } catch (err) {
    console.error("brazzers error:", err.message);
  }
  return results;
};
