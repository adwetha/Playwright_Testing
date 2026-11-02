from pathlib import Path
from playwright.sync_api import expect

def test_popup_window(page):
#step1:opem the local popup practice html Code
    html_file=Path(__file__).with_name("popup_practice.html")
    page.goto(html_file.resolve().as_uri())
    #step2:verify the original page
    expect(
        page.get_by_role("heading",name="Popup window practice")
    ).to_be_visible()
    #step3:Register popup extraction before clicking
    with.page.expect_popup() as popup_info:
        page.get_by_role(
            "button",name="Open Popup"
        ).click()
        #step4: Capture the popup page
        popup=popup_info.value
        #step5:Wait for the popup page to load
        #step 6:Verify the popup url
        expect(popup).to_have_url("http://example.com/")
        #step7:verify paragraph
        expect(popup).get_by_role("link", name="learn more").to_be_visible()
        print("popup test passed successfully")
       
