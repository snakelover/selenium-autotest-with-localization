from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_existence_on_localized_page(browser):
    browser.get(link)
    sleep(5)
    browser.find_element_by_class_name("btn-add-to-basket")
