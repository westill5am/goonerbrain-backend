const axios = require('axios');

module.exports = async function beeg(query) {
  const url = `https://api.beeg.com/api/v6/search/suggestions/${encodeURIComponent(query)}?site=beeg`;

  try {
    const { data } = await axios.get(url);
    const results = data.suggestions?.map(video => ({
      title: video.title,
      url: `https://beeg.com/${video.slug}`,
      duration: '',
      source: "Beeg"
    })) || [];

    return results;
  } catch (err) {
    console.error("beeg error:", err.message);
    return [];
  }
};
