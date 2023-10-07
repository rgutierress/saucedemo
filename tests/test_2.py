from pages.ProductsPage import ProductsPage


class Test2:

    def test_login_sourcedemo(self,open_browser):
        login_page = open_browser
        login_page.fill_form_login('standard_user','secret_sauce')
        login_page.click_login_btn()
        produtos_page = ProductsPage(login_page.driver)
        assert produtos_page.is_products_page(), 'URL da página de produtos inválida!'
        assert produtos_page.is_title_page()
        assert produtos_page.has_menu_icon(), 'Menu não encontrado!'
