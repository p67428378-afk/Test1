const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  try {
    console.log("Navigating to http://localhost:3000");
    await page.goto('http://localhost:3000');
    console.log("Successfully navigated to http://localhost:3000");
    // Add a small delay to ensure the page is fully loaded and rendered
    await page.waitForTimeout(2000);
    console.log("Page title:", await page.title());

  } catch (error) {
    console.error("Test Failed:", error);
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
