const axios = require('axios');
const cheerio = require('cheerio');

module.exports = async function keezmovies(query) {
  const url = `https://www.keezmovies.com/search/${encodeURIComponent(query)}`;
  const results = [];

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    $('.video').each((i, el) => {
      const title = $(el).find('.title').text().trim();
      const href = $(el).find('a').attr('href');
      const duration = $(el).find('.duration').text().trim();

      if (title && href) {
        results.push({
          title,
          url: 'https://www.keezmovies.com' + href,
          duration,
          source: "KeezMovies"
        });
      }
    });
  } catch (err) {
    console.error("keezmovies error:", err.message);
  }

  return results;
};