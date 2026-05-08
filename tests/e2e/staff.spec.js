const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;

test.describe('Reviewer & Chair Journeys @a11y', () => {
  test('reviewer evaluation form should be accessible', async ({ page }) => {
    // Mock or use test credentials
    await page.goto('/conta/entrar/');
    await page.fill('input[name="username"]', 'reviewer_test');
    await page.fill('input[name="password"]', 'password_test');
    await page.click('button[type="submit"]');

    // Go to a review page (example ID)
    await page.goto('/revisoes/avaliar/1/');
    
    const a11yResults = await new AxeBuilder({ page }).analyze();
    expect(a11yResults.violations).toEqual([]);
    
    // Check score rating labels
    const scoreLabel = page.locator('label:has-text("Nota (1-5)")');
    await expect(scoreLabel).toBeVisible();
  });

  test('chair dashboard should be accessible', async ({ page }) => {
    await page.goto('/conta/entrar/');
    await page.fill('input[name="username"]', 'chair_test');
    await page.fill('input[name="password"]', 'password_test');
    await page.click('button[type="submit"]');

    await page.goto('/painel/comissao/');
    const a11yResults = await new AxeBuilder({ page }).analyze();
    expect(a11yResults.violations).toEqual([]);
  });
});
