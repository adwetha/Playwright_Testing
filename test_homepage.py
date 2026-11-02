#understanding structure of playwright

from playwright.sync_api import expect

def test_homepage(page):
 page.goto("https://example.com/")
 expect(page).to_have_title("example")

