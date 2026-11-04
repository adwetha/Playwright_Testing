#Explicit wait using locator.wait_for()
from playwright.sync_api import expect
def test_dynamic_loading(page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.get_by_role("button",name="Start").click()
    heading=page.locator("#finish h4")
    heading.wait_for(
        state="visible",
        timeout=10000
    )
    expect(heading).to_have_text("Hello World!")
 
#waiting for navigation
from playwright.sync_api import expect
 
def test_wait_for_url(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button",name="Login").click()
    page.wait_for_url("**/secure")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
 
