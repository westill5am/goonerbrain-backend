const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function spankbangvr(query) {
  const url = `https://spankbang.com/s/${encodeURIComponent(query)}/1/?o=vr`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.video-item').each((i, el) => {
      const title = $(el).find('.title').text().trim();
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.dur').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://spankbang.com' + href,
          duration,
          source: "SpankBang VR"
        });
      }
    });
  } catch (err) {
    console.error("spankbangvr error:", err.message);
  }

  return results;
};