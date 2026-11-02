#multiple tabs in playwright
 
from playwright.sync_api import Page, expect
 
def test_multiple_tabs_basic(page: Page):
 
    #step 1: open first website
 
    page.goto("https://example.com")
 
    #Verify the first webpage
 
    expect(page).to_have_title("Example Domain")
 
    print("First tab URL: ", page.url)
 
    #Step 2: Create a second tab in same browser
 
    second_page = page.context.new_page()
 
    second_page.goto("https://www.wikipedia.org")
 
    #Verify the second website
 
    expect(second_page).to_have_title("Wikipedia")
 
    print("Second tab URL:", second_page.url)
 
    #Step 3: Verify the original tab is still open
 
    expect(page).to_have_title("Example Domain")
 
    #Step 4: Verify that two pages exist in the context
 
    all_pages = page.context.pages
 
    assert len(all_pages) == 2
 
    print("No.of open pages:", len(all_pages))
 
 
#multiple tabs in playwright
from playwright.sync_api import Page, expect
def test_multiple_tabs(page:Page):
 
        page.goto("https://example.com")
   
        #Verify the first webpage
   
        expect(page).to_have_title("Example Domain")
   
        print("First tab URL: ", page.url)
   
        #Step 2: Create a second tab in same browser
   
        second_page = page.context.new_page()
   
        second_page.goto("https://www.wikipedia.org")
   
        #Verify the second website
   
        expect(second_page).to_have_title("Wikipedia")
   
        print("Second tab URL:", second_page.url)
   
        #Step 3: Verify the original tab is still open
   
        expect(page).to_have_title("Example Domain")
   
        #Step 4: Verify that two pages exist in the context
   
        all_pages = page.context.pages
   
        assert len(all_pages) == 2
   
        print("No.of open pages:", len(all_pages))
   
   
        print("Second tab url:",second_page.url)
        #step 3: verify the orginal tab is stil open)
        expect(page).to_have_title("Example Domain")
        #step 4:verify that two pages exist in the context
        all_pages=page.context.pages
        assert len(all_pages)==2
        print("No.of open pages:",len(all_pages))
        #step 5: interact with the second tab
        expect(second_page.get_by_role("heading",name="Wikipedia")).to_be_visible()
        #step 6: close the second tab
        second_page.close()
        #step 7: verify the orginal tab remains open
        expect(page).to_have_title("Example Domain")
        assert len(page.context.pages)==1
        print("multiple tabs test passed successfully")
 
 
#Handling a new tab opened by clicking a link
 
#open the orginal website
#click the link
#capture the  new tab
#verify the new page
#interact with the new page
 
# from pathlib import Path
 
# from playwright.sync_api import expect
 
# def test_new_tab_from_link(page):
 
#     #Step 1: Open the local HTML page
 
#     html_file = Path(__file__).with_name("open_new_tab.html")
 
#     page.goto(html_file.resolve().as_uri())
 
#     #Step 2: Verify the originla page
 
#     expect(
 
#         page.get_by_role("heading", name="Original Page")
 
#     ).to_be_visible()
 
#     #Step 3: Verify thr link exists
 
#     link = page.get_by_role("link", name="Open Example Website in a New Tab")
 
#     expect(link).to_be_visible()
 
#     #Step 4: Click the link and capture new tab
 
#     with page.context.expect_page() as new_page_info:
 
#         link.click()
 
#     new_page = new_page_info.value
 
#     #Step 5:Wait for new tab to finish loading
 
#     new_page.wait_for_load_state("domcontentloaded")
 
#     #Step 6: Verify the new tab URL:
 
#     expect(new_page).to_have_url("https://example.com/")
 
#     print("Oringinal tab URL:", page.url)
 
#     print("New tab URL:", new_page.url)
 
#     #Step 7: Close the new tab
 
#     new_page.close()
 
#     print("New Tab test passed successfully.")
