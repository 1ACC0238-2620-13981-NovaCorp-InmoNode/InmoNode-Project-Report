/* Browser verification. Usage: node scripts/check_domain_flow_html.cjs [playwright-module-path]
 * Uses installed Microsoft Edge; screenshots go to .impeccable/review/.
 */
const { chromium } = require(process.argv[2] || 'playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const root = path.resolve(__dirname, '..');
const folder = path.join(root, 'assets/cap2/domain-message-flows');
const screenshots = path.join(root, '.impeccable/review');

(async () => {
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' });
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    const files = (await fs.readdir(folder)).filter(name => /^flow-.*\.html$/.test(name)).sort();
    assert.equal(files.length, 11);
    let routeCount = 0;
    let visited = 0;
    for (const file of files) {
      await page.goto(pathToFileURL(path.join(folder, file)).href);
      const flow = await page.locator('#flow-data').evaluate(node => JSON.parse(node.textContent));
      for (const route of flow.routes) {
        if (flow.routes.length > 1) await page.selectOption('#route-select', route.id);
        assert(await page.locator('#previous').isDisabled());
        for (let i = 0; i < route.steps.length; i++) {
          const message = flow.messages.find(row => row.step === route.steps[i]);
          assert.equal(await page.locator('#message-title').textContent(), message.name);
          assert.equal(await page.locator('#sender').textContent(), message.sender);
          assert.equal(await page.locator('#receiver').textContent(), message.receiver);
          assert.equal(await page.locator('#message-data').textContent(), message.data);
          assert.equal(await page.locator('#steps [aria-current="step"]').count(), 1);
          if (i < route.steps.length - 1) await page.click('#next');
          visited++;
        }
        assert(await page.locator('#next').isDisabled());
        await page.click('#previous');
        assert(!(await page.locator('#next').isDisabled()));
        await page.reload();
        assert.equal(await page.locator('#route-select').inputValue(), route.id);
        assert((await page.locator('#step-position').textContent()).startsWith(`Paso ${route.steps.length - 1} de`));
        if (await page.locator('#restart').isEnabled()) await page.click('#restart');
        assert(await page.locator('#previous').isDisabled());
        routeCount++;
      }
      for (const width of [1440, 390, 320]) {
        await page.setViewportSize({ width, height: 1000 });
        assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), `Overflow: ${file} at ${width}`);
      }
      await page.setViewportSize({ width: 1440, height: 1000 });
    }
    await page.goto(pathToFileURL(path.join(folder, 'flow-2B.html')).href);
    await page.keyboard.press('ArrowRight');
    assert((await page.locator('#step-position').textContent()).includes('2B.2'));
    await page.keyboard.press('ArrowLeft');
    assert(await page.locator('#previous').isDisabled());
    await page.locator('#steps button').nth(2).click();
    assert((await page.locator('#step-position').textContent()).includes('2B.3A'));
    await page.focus('#route-select');
    const previousStep = await page.locator('#step-position').textContent();
    const previousRoute = await page.locator('#route-select').inputValue();
    await page.keyboard.press('ArrowRight');
    if (await page.locator('#route-select').inputValue() === previousRoute) {
      assert.equal(await page.locator('#step-position').textContent(), previousStep, 'Arrow keys must respect select controls');
    } else {
      assert((await page.locator('#step-position').textContent()).startsWith('Paso 1 de'), 'A native route selection starts at its first step');
    }
    await page.selectOption('#flow-select', 'flow-1A.html');
    await page.waitForURL('**/flow-1A.html');
    assert((await page.title()).startsWith('1A'));
    await page.goto(pathToFileURL(path.join(folder, 'flow-2B.html')).href + '#ruta=invalid&paso=999');
    assert.equal(await page.locator('#route-select').inputValue(), 'aceptada');
    assert(await page.locator('#next').isDisabled());
    await page.goto(pathToFileURL(path.join(folder, 'index.html')).href);
    assert.equal(await page.locator('.directory-link').count(), 11);
    await page.locator('.directory-link').first().click();
    assert((await page.title()).startsWith('1A'));
    await fs.mkdir(screenshots, { recursive: true });
    await page.goto(pathToFileURL(path.join(folder, 'flow-2B.html')).href + '#ruta=aceptada&paso=2');
    await page.screenshot({ path: path.join(screenshots, 'desktop.png'), fullPage: true });
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(pathToFileURL(path.join(folder, 'flow-2F.html')).href + '#ruta=restablecida&paso=3');
    await page.screenshot({ path: path.join(screenshots, 'mobile.png'), fullPage: true });
    await page.emulateMedia({ media: 'print' });
    assert(await page.locator('.print-route').isVisible());
    assert.equal(await page.locator('#print-steps li').count(), 6);
    assert.deepEqual(errors, []);
    console.log(`Verified ${files.length} HTML files, ${routeCount} routes, ${visited} steps, keyboard navigation, deep links, print and responsive layout.`);
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode = 1; });
