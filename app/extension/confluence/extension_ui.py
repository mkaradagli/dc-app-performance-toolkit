from selenium.webdriver.common.by import By
from selenium_ui.conftest import print_timing
from util.conf import CONFLUENCE_SETTINGS

from selenium_ui.base_page import BasePage

def selenium_app_add_label(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_add_label")
    def measure():

        @print_timing("selenium_app_add_label:view_page")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/plugins/spacelabelmanager/spacepagebulklabeloperations.action?key=TEST")
            page.wait_until_visible((By.ID, "token-input-newLabelText"))  # Wait for title field visible
            page.wait_until_visible((By.ID, "token-input-newLabelText")).click()
            page.wait_until_visible((By.ID, "token-input-newLabelText")).send_keys("admin ")
            page.wait_until_visible((By.ID, "next")).click()
            page.wait_until_visible((By.ID, "tree-selection-next")).click()
            page.wait_until_visible((By.ID, "confirm-next")).click()
            page.wait_until_visible((By.CLASS_NAME, "aui-message-confirmation"))
        sub_measure()
    measure()

def selenium_app_replace_label(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_replace_label")
    def measure():

        @print_timing("selenium_app_replace_label:view_page")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/plugins/spacelabelmanager/spacepagebulklabeloperations.action?key=TEST")
            page.wait_until_visible((By.ID, "replace-label-tab-link")).click()
            page.wait_until_visible((By.ID, "replace-label-form"))  # Wait for title field visible
            page.wait_until_visible((By.XPATH, "//form[@id='replace-label-form']//input[@id='token-input-removeLabelText']")).click()
            page.wait_until_visible((By.XPATH, "//form[@id='replace-label-form']//input[@id='token-input-removeLabelText']")).send_keys("admin ")
            page.wait_until_visible((By.ID, "replace-label-tab-link")).click()
            page.wait_until_visible((By.XPATH, "//form[@id='replace-label-form']//input[@id='token-input-newLabelText']")).click()
            page.wait_until_visible((By.XPATH, "//form[@id='replace-label-form']//input[@id='token-input-newLabelText']")).send_keys("asd ")
            page.wait_until_visible((By.ID, "replace-label-tab-link")).click()
            page.wait_until_visible((By.XPATH, "//form[@id='replace-label-form']//button[@id='next']")).click()
            page.wait_until_visible((By.ID, "tree-selection-next")).click()
            page.wait_until_visible((By.ID, "confirm-next")).click()
            page.wait_until_visible((By.CLASS_NAME, "aui-message-confirmation"))
        sub_measure()
    measure()

    
def selenium_app_remove_label(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_remove_label")
    def measure():

        @print_timing("selenium_app_remove_label:view_page")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/plugins/spacelabelmanager/spacepagebulklabeloperations.action?key=TEST")
            page.wait_until_visible((By.ID, "remove-label-tab-link")).click()
            page.wait_until_visible((By.ID, "remove-label-form"))  # Wait for title field visible
            page.wait_until_visible((By.XPATH, "//form[@id='remove-label-form']//input[@id='token-input-removeLabelText']")).click()
            page.wait_until_visible((By.XPATH, "//form[@id='remove-label-form']//input[@id='token-input-removeLabelText']")).send_keys("asd ")
            page.wait_until_visible((By.ID, "remove-label-tab-link")).click()
            page.wait_until_visible((By.XPATH, "//form[@id='remove-label-form']//button[@id='next']")).click()
            page.wait_until_visible((By.ID, "tree-selection-next")).click()
            page.wait_until_visible((By.ID, "confirm-next")).click()
            page.wait_until_visible((By.CLASS_NAME, "aui-message-confirmation"))
        sub_measure()
    measure()