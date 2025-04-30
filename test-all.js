const fs = require('fs');
const path = require('path');

const testQuery = "milf"; // your test keyword
const scraperDir = __dirname;

(async () => {
  const files = fs.readdirSync(scraperDir).filter(f => f.endsWith('.js') && f !== 'test-all.js');
  console.log(`🔍 Testing ${files.length} scrapers with query "${testQuery}"\n`);
  for (const file of files) {
    try {
      const scraper = require(path.join(scraperDir, file));
      const results = await scraper(testQuery);
      const count = Array.isArray(results) ? results.length : 0;
      console.log(`✅ ${file} returned ${count} results`);
    } catch (err) {
      console.log(`❌ ${file} failed: ${err.message}`);
    }
  }
})();
