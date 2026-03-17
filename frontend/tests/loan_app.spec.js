import { test, expect } from '@playwright/test';

test.describe('Loan Application Platform', () => {
  test('should allow user to submit a loan application', async ({ page }) => {
    await page.goto('http://localhost:3000');

    // Expect a title "to contain" a substring.
    await expect(page).toHaveTitle(/Loan Application Platform/);

    // Fill in personal information
    await page.fill('#first_name', 'John');
    await page.fill('#last_name', 'Doe');
    await page.fill('#email', 'john.doe@example.com');
    await page.fill('#phone_number', '123-456-7890');
    await page.fill('#date_of_birth', '1990-01-01');
    await page.fill('#address', '123 Main St, Anytown, USA');

    // Fill in loan details
    await page.fill('#loan_amount', '25000');
    await page.fill('#loan_tenure', '48');

    // Fill in financial information
    await page.fill('#financial_details', 'Annual Income: $70,000, Employment: Full-time, Existing Loan: $5,000');

    // Fill in bank details
    await page.fill('#bank_details', 'Bank of Playwright, 9876543210, PLWGUS3N');

    // Agree to legal terms
    await page.check('#legal_consent');

    // Submit application
    await page.click('button[type="submit"]');

    // Expect success message
    await expect(page.locator('.message.success')).toContainText('Application submitted successfully');
  });

  test('should display loan officer dashboard', async ({ page }) => {
    await page.goto('http://localhost:3000/officer-dashboard');

    // Expect dashboard title
    await expect(page.locator('h2')).toContainText('Loan Officer Dashboard');

    // Assuming there's at least one application submitted from the previous test or pre-existing data
    // Check for an application card
    await expect(page.locator('.application-card')).toBeVisible();

    // Check for approve/reject buttons on a pending application
    await expect(page.locator('.application-card .approve-btn')).toBeVisible();
    await expect(page.locator('.application-card .reject-btn')).toBeVisible();
  });
});
