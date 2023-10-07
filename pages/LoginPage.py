import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.ProductsPage import ProductsPage


class LoginPage:

    url = 'https://www.saucedemo.com/'

    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_page(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()

    def click_login_btn(self):
        self.driver.find_element(By.ID, 'login-button').click()

    def is_url(self):
        return self.driver.current_url == self.url

    def has_login_error_message(self):
        error_message = self.driver.find_element(By.CLASS_NAME, 'error-message-container').text
        return error_message == 'Epic sadface: Username is required'

    def fill_form_login(self,name,password):
        self.driver.find_element(By.ID, 'user-name').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys(password)
