import time


class TestAuthorization:

    # test RT-001
    def test_base_page(self, auth):
        """Загрузка главной страницы сайта"""
        auth.go_to_sait()
        url = auth.get_current_url()
        try:
            assert url == 'https://b2c.passport.rt.ru/'
        except:
            print('test RT-001 ERROR')

    # test RT-010
    def test_way_authorization_email(self, auth):
        """Проверка выбора способа авторизации по email"""
        auth.go_to_sait()
        auth.click_to_way_email()
        text_field_username = auth.get_text_field_username()
        try:
            assert text_field_username == 'Электронная почта'
        except:
            print('test RT-010 ERROR. ')

    # test RT-011
    def test_way_authorization_login(self, auth):
        """Проверка выбора способа авторизации по login"""
        auth.go_to_sait()
        auth.click_to_way_login()
        text_field_username = auth.get_text_field_username()
        try:
            assert text_field_username == 'Логин'
        except:
            print('test RT-011 ERROR')

    # test RT-012
    def test_way_authorization_ls(self, auth):
        """Проверка выбора способа авторизации по ls"""
        auth.go_to_sait()
        auth.click_to_way_ls()
        text_field_username = auth.get_text_field_username()
        try:
            assert text_field_username == 'Лицевой счёт'
        except:
            print('test RT-012 ERROR')

    # test RT-013
    def test_way_authorization_phone(self, auth):
        """Проверка выбора способа авторизации по phone"""
        auth.go_to_sait()
        auth.click_to_way_ls()
        auth.click_to_way_phone()
        text_field_username = auth.get_text_field_username()
        try:
            assert text_field_username == 'Мобильный телефон'
        except:
            print('test RT-013 ERROR')

    # test RT-014
    def test_show_pass(self, auth):
        """Проверка кнопки показать/скрыть пароль"""
        auth.go_to_sait()
        auth.send_password()
        auth.click_show_pass()
        time.sleep(3)
        try:
            assert auth.get_sow_pass()
        except:
            print('test RT-014 ERROR')

    # test RT-015
    def test_auth_for_phone(self, auth):
        """Авторизация с валидными данными по номеру телефона"""
        auth.go_to_sait()
        auth.send_phone()
        auth.send_password()
        auth.click_button_enter()
        try:
            assert auth.get_logout()
        except:
            print('test RT-015 ERROR')

    # test RT-016
    def test_auth_with_invalid_password(self, auth):
        """Авторизация по телефону с неправильным паролем"""
        auth.go_to_sait()
        auth.send_phone()
        auth.send_invalid_password()
        auth.click_button_enter()
        text = auth.get_text_error_message_auth()
        try:
            assert text == 'Неверный логин или пароль'
        except:
            print('test RT-016 ERROR')

    # test RT-017
    def test_auth_for_email(self, auth):
        """Авторизация с валидными данными по электронной почте"""
        auth.go_to_sait()
        auth.click_to_way_email()
        auth.send_email()
        auth.send_password()
        auth.click_button_enter()
        try:
            assert auth.get_logout()
        except:
            print('test RT-017 ERROR')

    # test RT-018
    def test_recovery_pass_phone(self, auth):
        """Проверка перехода на страницу восстановления пароля"""
        auth.go_to_sait()
        auth.click_forgot_password()
        try:
            assert auth.get_button_go_back()
        except:
            print('test RT-018 ERROR')

    # test RT-021
    def test_button_vk(self, auth):
        auth.go_to_sait()
        auth.click_button_vk()
        url = auth.get_current_url()
        url_mod = url.partition('authorize')[0]
        try:
            assert url_mod == 'https://oauth.vk.com/'
        except:
            print('test RT-021 ERROR')

    # test RT-022
    def test_button_OK(self, auth):
        auth.go_to_sait()
        auth.click_button_ok()
        url = auth.get_current_url()
        url_mod = url.partition('/dk')[0]
        try:
            assert url_mod == 'https://connect.ok.ru'
        except:
            print('test RT-022 ERROR')

    # test RT-023
    def test_button_mm(self, auth):
        auth.go_to_sait()
        auth.click_button_mm()
        url = auth.get_current_url()
        url_mod = url.partition('oauth/authorize')[0]
        try:
            assert url_mod == 'https://connect.mail.ru/'
        except:
            print('test RT-023 ERROR')

    # test RT-024
    def test_button_google(self, auth):
        auth.go_to_sait()
        auth.click_button_google()
        url = auth.get_current_url()
        url_mod = url.partition('o/oauth2')[0]
        try:
            assert url_mod == 'https://accounts.google.com/'
        except:
            print('test RT-024 ERROR')

    # test RT-025
    def test_button_yandex(self, auth):
        auth.go_to_sait()
        auth.click_button_yandex()
        url = auth.get_current_url()
        url_mod = url.partition('auth')[0]
        try:
            assert url_mod == 'https://b2c.passport.rt.ru/'
        except:
            print('test RT-025 ERROR')
