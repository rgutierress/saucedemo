import pytest
from selenium import webdriver

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage

URL = 'https://www.saucedemo.com/'


@pytest.fixture
def open_browser():

    login_page = LoginPage()
    login_page.open_page()
    yield login_page # Tudo que é executado após o yield será executado depois do teste
    login_page.close()