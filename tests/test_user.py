def test_username(user_data):
 assert user_data["username"]=="testuser"
 assert user_data["password"]=="test123"

#Basic python assertion
def test_username():
 username="admin"
 assert username=="admin"
def test_values():
 assert 10 > 5
 assert "Python" in "Python playwright"
 assert 5 !=3
 assert [1,2,3] ==[1,2,3]

#Parameterization - testing multiple inputs
import pytest

@pytest.mark.parametrize(
    "number,expected",
    [
        (2,4),
        (3,9),
        (4,16)
    ]
)
def test_square(number,expected):
    assert number * number == expected

import pytest

@pytest.mark.smoke
def test_homepage_title():
    assert "Home" == "Home"

@pytest.mark.regression
def test_user_status():
    assert "Active" == "Active"

#create our first test
# from playwright.sync_api import expect

# def test_amazon_homepage(page):
#     response = page.goto(
#         "https://www.amazon.com",
#         wait_until="domcontentloaded",
#         timeout=15000
#     )

#     print("response status:", response.status if response else None)
#     print("Page title:", repr(page.title()))
#     print("Current url:", page.url)
#     print("page content:", page.locator("body").inner_text()[:500])

#     expect(page).to_have_title(
#         "Amazon.com. Spend less. Smile.more.",
#         timeout=15000
#     )

#Example: click a button
from playwright.sync_api import expect

def test_click_button(page):
    page.goto("https://www.playwrightautomation.com/practice.html")

    button = page.get_by_role("button", name="Submit")
    expect(button).to_be_visible()
    button.click()

#to_have_value
from playwright.sync_api import expect

def test_username_input(page):
    page.goto("https://www.playwrightautomation.com/practice.html")

    name_input = page.get_by_placeholder("enter your name")
    name_input.fill("vikas")

    expect(name_input).to_have_value("vikas")

#Text Extraction
def test_extract_heading(page):
    page.goto("https://the-internet.herokuapp.com/")

    heading = page.locator("h1").inner_text()
    print(heading)

    assert heading == "Welcome to the-internet"

#Text content
def test_extract_heading(page):
    page.goto("https://the-internet.herokuapp.com/")

    heading = page.locator("h1").text_content()
    print(heading)

    assert heading == "Welcome to the-internet"

#Difference between assert and expect
from playwright.sync_api import expect

def test_heading(page):
    page.goto("https://the-internet.herokuapp.com/")

    heading = page.locator("h1")
    expect(heading).to_have_text("Welcome to the-internet")

#all_text_content
def test_heading(page):
    page.goto("https://the-internet.herokuapp.com/")

    links = page.locator("ul li a").all_text_contents()
    print(links)

    assert len(links) > 0

#get_attribute(href)
def test_heading(page):
    page.goto("https://the-internet.herokuapp.com/")

    href = page.get_by_role(
        "link",
        name="Subdirectories"
    ).get_attribute("href")

    print(href)

# #expect assertion in playwright
from playwright.sync_api import expect

def test_successful_login(page):
    page.goto("https://the-internet.herokuapp.com/login")

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")

    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/secure"
    )

    expect(page.locator("#flash")).to_contain_text(
        "You logged into a secure area!"
    )

    expect(
        page.get_by_role(
            "heading",
            name="Secure Area",
            exact=True
        )
    ).to_be_visible()



 
# #################26/10/2026######################
 
# from playwright.sync_api import Page, expect
# def test_zoom_meeting_registration(page: Page):
#     #Step 1: Open Zoom registration page
#     page.goto("https://ust.zoom.us/meeting/register/wROkcnzOSO2Z7jeg-vMTPA#/registration")
#     #Step 2: Enter First Name
#     page.get_by_label("First Name").fill("Vikas")
#     #Step 3: Enter Last Name
#     page.get_by_label("Last Name").fill("P")
#     #Step 4: Email
#     page.get_by_label("Email Address").fill("vikasp@gmail.com")
#     #Step 5: Enter UST UID
#     page.get_by_label("UST UID").fill("123456")
#     #Step 6: Verify the entered info
#     expect(page.get_by_label("First Name")).to_have_value("Vikas")
#     expect(page.get_by_label("Last Name")).to_have_value("P")
#     expect(page.get_by_label("Email Address")).to_have_value("vikasp@gmail.com")
#     expect(page.get_by_label("UST UID")).to_have_value("123456")
#     #Step 7: Locate the Resigter and Join Button
#     register_button = page.get_by_role("button", name="Register and Join")
#     #Step 8: Verify the button is visible
#     expect(register_button).to_be_visible()
 
 
 
 
 
from playwright.sync_api import Page, expect
def test_native_dropdown(page):
    # Step 1: Open URL
    page.goto("https://practice.expandtesting.com/dropdown")
 
    # Step 2: Locate the simple dropdown
    dropdown = page.locator("#dropdown")
 
    # Step 3: Verify the dropdown is visible or not
    expect(dropdown).to_be_visible()
 
    # Step 4: Select option using its value
    dropdown.select_option("1")
 
    # Step 5: Verify selected value
    expect(dropdown).to_have_value("1")
 
    # Step 6: Select another option
    dropdown.select_option("2")
 
    # Step 7: Verify new selected value
    expect(dropdown).to_have_value("2")
 
    print("Dropdown options were selected successfully")
 
 

 

 
