const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;

test.describe('Author Journey @a11y', () => {
  test('should login and view dashboard with no a11y violations', async ({ page }) => {
    // Navigate to Login
    await page.goto('/conta/entrar/');
    
    // Fill credentials (placeholders)
    await page.fill('input[name="username"]', 'author_test');
    await page.fill('input[name="password"]', 'password_test');
    await page.click('button[type="submit"]');

    // Wait for Dashboard
    await expect(page).toHaveURL(/\/painel\//);
    
    // Check Dashboard Accessibility
    const dashboardA11yResults = await new AxeBuilder({ page }).analyze();
    expect(dashboardA11yResults.violations).toEqual([]);

    // Check Submission Wizard Step 1
    await page.goto('/submissoes/novo/');
    const wizardA11yResults = await new AxeBuilder({ page }).analyze();
    expect(wizardA11yResults.violations).toEqual([]);
    
    // Verify ARIA attributes on invalid submission
    await page.click('button:has-text("Próximo")');
    const titleError = page.locator('#id_title-error');
    await expect(titleError).toBeVisible();
    await expect(page.locator('#id_title')).toHaveAttribute('aria-invalid', 'true');
    await expect(page.locator('#id_title')).toHaveAttribute('aria-describedby', /id_title-error/);
  });
});
