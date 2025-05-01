const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function(query) {
  const url = `https://spankbang.party/s/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0'
      }
    });

    const $ = cheerio.load(data);

    $('div.video-list > a').each((_, el) => {
      const href = $(el).attr('href');
      const title = $(el).find('.title').text().trim();
      const preview = $(el).find('img').attr('data-src') || $(el).find('img').attr('src');
      const duration = $(el).find('.dur').text().trim();

      if (href && title && preview) {
        results.push({
          title,
          url: `https://spankbang.party${href}`,
          preview: preview.startsWith('http') ? preview : `https:${preview}`,
          duration,
          source: 'SpankBang'
        });
      }
    });

    return results;
  } catch (err) {
    console.error('❌ SpankBang scraper error:', err.message);
    return [];
  }
};
