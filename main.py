from RPA.Browser.Selenium import Selenium
#from RPA.Outlook.Application import Application
from RPA.Desktop import Desktop
from RPA.Dialogs import Dialogs
desktop = Desktop()

browser = Selenium()
url = "https://robocorp.com/docs/"
term = "python"
screenshot_filename = "output/screenshot.png"


def open_the_website(url: str):
    browser.open_available_browser(url)


def search_for(term: str):
    input_field = "css:input"
    browser.input_text(input_field, term)
    browser.press_keys(input_field, "ENTER")


def store_screenshot(filename: str):
    browser.screenshot(filename=filename)


def write_entry_in_accounting(entry):
    desktop.open_application("C:\Program Files\DBeaver\dbeaver.exe")
    desktop.click(f"image:{ROBOT_ROOT}/images/create.png")
    desktop.type_text(entry)
    desktop.press_keys("ctrl", "s")
    desktop.press_keys("enter")


from RPA.Excel.Application import Application

def excel_rpa():
    app = Application()
    app.open_application()
    app.open_workbook('input/Prueba.xlsx')
    app.set_active_worksheet(sheetname='Hoja')
    app.write_to_cells(row=1, column=1, value='new data')
    app.save_excel()
    app.quit_application()
import os


# Define a main() function that calls the other functions in order:
def main():
    try:
        print(os.path.dirname(os.path.abspath(__file__)))
        open_the_website(url)
        search_for(term)
        store_screenshot(screenshot_filename)
        excel_rpa()
        #write_entry_in_accounting('s')
    finally:
        browser.close_all_browsers()

# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()