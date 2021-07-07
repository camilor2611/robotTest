from task.RobotBrowser import AutomateBrowser
from task.AdminFileSystem import CopyInWorkSpace
from RPA.Excel.Application import Application

NAME_ASSISTANT = 'FirstTest'
PATH_WORKSPACE = 'C:/robots/'

url = "https://robocorp.com/docs/"
term = "python"

def main():
    admin_work_space = CopyInWorkSpace(PATH_WORKSPACE + NAME_ASSISTANT + '/')
    path_input, path_output = admin_work_space.get_main_folders()
    admin_work_space.copy_files_input_to_output()
    browser_chrome = AutomateBrowser()
    browser_chrome.open_the_website(url)
    browser_chrome.search_for(term)
    screenshot_filename = "screenshot.png"
    browser_chrome.store_screenshot(path_output + screenshot_filename)
    app = Application()
    app.open_application()
    app.open_workbook(path_output + 'Prueba.xlsx')
    app.set_active_worksheet(sheetname='Hoja')
    app.write_to_cells(row=1, column=1, value='new data')
    app.save_excel()
    app.quit_application()

        #excel_rpa()
        #write_entry_in_accounting('s')
    #finally:
    browser_chrome.automate_browser.close_all_browsers()
        #browser_chrome.close_all_browsers()
if __name__ == "__main__":
    main()