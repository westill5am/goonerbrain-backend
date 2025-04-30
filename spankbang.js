const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function spankbang(query) {
  const url = `https://spankbang.party/s/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('a.video').each((i, el) => {
      const title = $(el).find('.title').text().trim();
      const videoUrl = 'https://spankbang.party' + $(el).attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && videoUrl) {
        results.push({
          title,
          url: videoUrl,
          duration,
          source: "SpankBang"
        });
      }
    });
  } catch (err) {
    console.error("spankbang error:", err.message);
  }

  return results;
};
