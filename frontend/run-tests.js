const { chromium } = require('playwright');
const { test, expect } = require('@playwright/test');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  try {
    // Test 1: Loan Application Submission
    await page.goto('http://localhost:3000');
    await expect(page).toHaveTitle(/Loan Application Platform/);

    await page.fill('#first_name', 'John');
    await page.fill('#last_name', 'Doe');
    await page.fill('#email', 'john.doe@example.com');
    await page.fill('#phone_number', '123-456-7890');
    await page.fill('#date_of_birth', '1990-01-01');
    await page.fill('#address', '123 Main St, Anytown, USA');
    await page.fill('#loan_amount', '25000');
    await page.fill('#loan_tenure', '48');
    await page.fill('#financial_details', 'Annual Income: $70,000, Employment: Full-time, Existing Loan: $5,000');
    await page.fill('#bank_details', 'Bank of Playwright, 9876543210, PLWGUS3N');
    await page.check('#legal_consent');
    await page.click('button[type="submit"]');
    await expect(page.locator('.message.success')).toContainText('Application submitted successfully');
    console.log("Test 1 Passed: Loan application submitted successfully.");

    // Test 2: Loan Officer Dashboard
    await page.goto('http://localhost:3000/officer-dashboard');
    await expect(page.locator('h2')).toContainText('Loan Officer Dashboard');
    await expect(page.locator('.application-card')).toBeVisible();
    await expect(page.locator('.application-card .approve-btn')).toBeVisible();
    await expect(page.locator('.application-card .reject-btn')).toBeVisible();
    console.log("Test 2 Passed: Loan officer dashboard displayed correctly.");

  } catch (error) {
    console.error("Test Failed:", error);
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
