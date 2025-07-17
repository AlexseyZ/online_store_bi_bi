from playwright.sync_api import Page

class BasePage:
    url = None

    def __init__(self, page: Page):
        self.page = page

    def open_home_page(self):
        if self.url:
            self.page.goto(self.url)
        else:
            print(f'Страница не открывается по адресу {self.url}')
