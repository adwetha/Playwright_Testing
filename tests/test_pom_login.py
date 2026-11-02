from playwright.sync_api import Page,expect
from pages.login_page import LoginPage

def test_successful_login(page:Page):
    #create the page object
    login_page=LoginPage(page)
    #open the application
    login_page.open()
    #Login using valid credentials
    login_page.login("standard_user","secret_sauce")
    #verify successful login
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Products",exact=True)).to_be_visible()
