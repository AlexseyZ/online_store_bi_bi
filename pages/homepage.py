import allure
from playwright.sync_api import expect, Page
from pages.basepage import BasePage


class HomePage(BasePage):
    url = "https://bi-bi.ru/"


    def click_button_select_parts_car(self):
        self.page.locator("//span[@class='d-sm-none d-md-inline-block']").click()

    def click_button_pickup_goods(self):
        self.page.locator("//span[@class='js-mode-name']").click()







