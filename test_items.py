import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#time.sleep(30)

def test_check_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    elements_button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert elements_button > 0, "The button is NOT found"