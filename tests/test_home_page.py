import pytest
import allure
from pages.homepage import HomePage

from playwright.sync_api import expect, Page


@allure.title("Открыть страницу автомагазина Би-Би")
def test_open_home_page(page: Page):
    #Создали объект класса HomePage и передали ему аргумент page
    home_page = HomePage(page)
    home_page.open_home_page()
