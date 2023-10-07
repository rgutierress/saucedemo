class Test1:

    def test_click_login_button(self, open_browser):
        login_page = open_browser
        login_page.click_login_btn()
        assert login_page.is_url(),'Aplicação não permaneceu na mesma página'
        assert login_page.has_login_error_message(), 'Mensagem de erro inválida'