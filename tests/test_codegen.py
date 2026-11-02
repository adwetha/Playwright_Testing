import re
from playwright.sync_api import Playwright, sync_playwright, expect
 
 
def test_login() -> None:
 with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
 
 
 
#     # ---------------------
#     # context.close()
#     browser.close()
 
 
# # with sync_playwright() as playwright:
# #     run(playwright)
 
from playwright.sync_api import sync_playwright, expect
 
from playwright.sync_api import Page, expect
 
def test_login(page: Page) -> None:
 
    page.goto("https://www.saucedemo.com/")
 
    page.locator('[data-test="username"]').fill("standard_user")
 
    page.locator('[data-test="password"]').fill("secret_sauce")
 
    page.locator('[data-test="login-button"]').click()
 
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")