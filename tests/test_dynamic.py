from pages.dynamic_page import DynamicPage

def test_dynamic_loading(browser):
    dynamic_page=DynamicPage(browser)

    dynamic_page.open_example(example_id=1)
    dynamic_page.start_loading()
    dynamic_page.wait_for_loading_to_finish()
    assert dynamic_page.get_final_text() == "Hello World!","Text not displayed!"

    dynamic_page.open_example(example_id=2)
    dynamic_page.start_loading()
    dynamic_page.wait_for_loading_to_finish()
    assert dynamic_page.get_final_text() =="Hello World!","Text not displayed!"
