

class TestRegistration:

    # test RT-002
    def test_registr_page(self, browser, auth, registr):
        """Загрузка страницы авторизации"""
        auth.go_to_sait()
        auth.click_to_registration()
        url = auth.get_current_url()
        try:
            url == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/' \
                   'registration?client_id=account_b2c&tab_id=_w1HMLwkBtM'
        except:
            print('test RT-002 ERROR')

    # test RT-003
    def test_registration_valid_email(self, browser, auth, registr):
        """Проверка регистрации с валидными данными используя email"""
        auth.go_to_sait()
        auth.click_to_registration()
        registr.send_name()
        registr.send_last_name()
        registr.send_email()
        registr.send_password()
        registr.send_double_password()
        registr.click_button_registr()
        text = registr.get_text()
        try:
            assert text == 'Подтверждение email'
        except:
            print('test RT-003 ERROR')

    # test RT-004
    def test_registration_double_email(self, browser, auth, registr):
        """Проверка регистрации с валидными данными и уже зарегистрированным email"""
        auth.go_to_sait()
        auth.click_to_registration()
        registr.send_name()
        registr.send_last_name()
        registr.send_registr_email()
        registr.send_password()
        registr.send_double_password()
        registr.click_button_registr()
        text = registr.get_text_enter()
        try:
            assert text == "Войти"
        except:
            print('test RT-004 ERROR')

    # test RT-005
    def test_registration_phone(self, browser, auth, registr):
        """Проверка регистрации с валидными данными используя телефонный номер"""
        auth.go_to_sait()
        auth.click_to_registration()
        registr.send_name()
        registr.send_last_name()
        registr.send_phone()
        registr.send_password()
        registr.send_double_password()
        registr.click_button_registr()
        text = registr.get_text()
        try:
            assert text == 'Подтверждение телефона'
        except:
            print('test RT-005 ERROR')

    # test RT-006
    def test_registration_double_phone(self, browser, auth, registr):
        """Проверка регистрации с валидными данными и уже зарегистрированным номером телефона"""
        auth.go_to_sait()
        auth.click_to_registration()
        registr.send_name()
        registr.send_last_name()
        registr.send_registr_phone()
        registr.send_password()
        registr.send_double_password()
        registr.click_button_registr()
        text = registr.get_text_enter()
        try:
            assert text == "Войти"
        except:
            print('test RT-006 ERROR')

    # test RT-007
    def test_7symbol_password_registration(self, browser, auth, registr):
        """Ввод в поле пароль при регистрации строки длиной семь знаков"""
        auth.go_to_sait()
        auth.click_to_registration()
        registr.send_name()
        registr.send_last_name()
        registr.send_email()
        registr.send_7symbol_pass()
        registr.send_7symbol_double_pass()
        registr.click_button_registr()
        text_error_pass = registr.get_error_pass()
        text_error_double_pass = registr.get_error_double_pass()
        try:
            assert text_error_pass == 'Длина пароля должна быть не менее 8 символов'
            assert text_error_double_pass == 'Длина пароля должна быть не менее 8 символов'
        except:
            print('test RT-007 ERROR')

    # test RT-008
    def test_21symbol_password_registration(self, browser, auth, registr):
        """Ввод в поле пароль при регистрации строки длиной двадцать один знак"""
        auth.go_to_sait()
        auth.click_to_registration()
        registr.send_name()
        registr.send_last_name()
        registr.send_email()
        registr.send_21symbol_pass()
        registr.send_21symbol_double_pass()
        registr.click_button_registr()
        text_error_pass = registr.get_error_pass()
        text_error_double_pass = registr.get_error_double_pass()
        try:
            assert text_error_pass == 'Длина пароля должна быть не более 20 символов'
            assert text_error_double_pass == 'Длина пароля должна быть не более 20 символов'
        except:
            print('test RT-008 Error')

    # test RT-009
    def test_20symbol_password_registration(self, browser, auth, registr):
        """Ввод в поле пароль при регистрации строки длиной двадцать знаков"""
        auth.go_to_sait()
        auth.click_to_registration()
        registr.send_name()
        registr.send_last_name()
        registr.send_phone()
        registr.send_20symbol_pass()
        registr.send_20symbol_double_pass()
        registr.click_button_registr()
        text = registr.get_text()
        try:
            assert text == 'Подтверждение телефона'
        except:
            print('test RT-009 ERROR')

