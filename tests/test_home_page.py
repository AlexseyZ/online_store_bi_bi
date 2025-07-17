import pytest
import allure
from pages.homepage import HomePage

from playwright.sync_api import expect, Page


@allure.title("Открыть страницу автомагазина Би-Би")
def test_open_home_page(page: Page):
    # Создали объект класса HomePage и передали ему аргумент page
    home_page = HomePage(page)
    home_page.open_home_page()
    expect(page.locator("//a[@class='header-top__logo']")).to_be_visible()


@allure.title("Нажать кнопку [Подобрать детали под автомобиль]")
def test_click_button_select_parts_car(page: Page):
    home_page = HomePage(page)
    home_page.open_home_page()
    home_page.click_button_select_parts_car()
    expect(page.locator("(//h3[contains(text(),'Подбор по автомобилю')])[1]")).to_be_visible()


@allure.title("Нажать на кнопку [Самовывоз товара из магазина]")
def test_button_pickup_goods(page: Page):
    home_page = HomePage(page)
    home_page.open_home_page()
    home_page.click_button_pickup_goods()
    expect(page.locator("(//div[@class='modal-title h2'])[2]")).to_be_visible()
