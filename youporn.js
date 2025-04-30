const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function youporn(query) {
  const url = `https://www.youporn.com/results/?query=${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url, {
      headers: {
        'User-Agent':
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Safari/537.36'
      }
    });

    const $ = cheerio.load(data);

    $('div.video-wrapper').each((i, el) => {
      const title = $(el).find('.video-title a').text().trim();
      const href = $(el).find('.video-title a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://www.youporn.com' + href,
          duration,
          source: 'YouPorn'
        });
      }
    });
  } catch (err) {
    console.error('youporn error:', err.message);
  }

  return results;
};
