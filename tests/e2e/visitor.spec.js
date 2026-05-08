const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;

test.describe('Visitor Journey @a11y', () => {
  test('should navigate through public pages with no a11y violations', async ({ page }) => {
    await page.goto('/');
    
    // Check Home Page
    const homeA11yResults = await new AxeBuilder({ page }).analyze();
    expect(homeA11yResults.violations).toEqual([]);

    // Navigate to Program
    await page.click('text=Programação');
    await expect(page).toHaveURL(/\/programacao\//);
    
    const programA11yResults = await new AxeBuilder({ page }).analyze();
    expect(programA11yResults.violations).toEqual([]);

    // Check Submissions Info
    await page.goto('/submissoes/');
    const submissionsA11yResults = await new AxeBuilder({ page }).analyze();
    expect(submissionsA11yResults.violations).toEqual([]);
  });

  test('should have a working skip link', async ({ page }) => {
    await page.goto('/');
    await page.keyboard.press('Tab');
    const skipLink = page.locator('text=Pular para o conteúdo principal');
    await expect(skipLink).toBeVisible();
    await skipLink.click();
    await expect(page.locator('#main-content')).toBeFocused();
  });
});
