import allure
from playwright.sync_api import expect, Page


class HomePage:

    def __init__(self, page):
        self.page = page

    def open_home_page(self):
        self.page.goto("https://bi-bi.ru/")
        expect(self.page.locator("//a[@class='header-top__logo']")).to_be_visible()

