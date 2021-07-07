from RPA.Browser.Selenium import Selenium

class AutomateBrowser():
    def __init__(self):
        self.automate_browser = Selenium()

    def open_the_website(self, url: str):
        self.automate_browser.open_available_browser(url)

    def search_for(self, term: str):
        input_field = "css:input"
        self.automate_browser.input_text(input_field, term)
        self.automate_browser.press_keys(input_field, "ENTER")

    def store_screenshot(self, file_name: str):
        self.automate_browser.screenshot(filename=file_name)