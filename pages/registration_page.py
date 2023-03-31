from pages.locator_page import LocatorRegistration
from pages.base_page import BasePage


class Registration(BasePage, LocatorRegistration):

    def send_name(self):
        return self.find_element(self.LOCATOR_NAME).send_keys('Белла')

    def send_last_name(self):
        return self.find_element(self.LOCATOR_LAST_NAME).send_keys('Лучко')

    def send_email(self):
        return self.find_element(self.LOCATOR_EMAIL_PHONE).send_keys('xo4yshe4ka3@yandex.ru')

    def send_registr_email(self):
        return self.find_element(self.LOCATOR_EMAIL_PHONE).send_keys('xo4yshe4ka@yandex.ru')

    def send_password(self):
        return self.find_element(self.LOCATOR_PASSWORD).send_keys('A12345678aA')

    def send_double_password(self):
        return self.find_element(self.LOCATOR_DOUBLE_PASSWORD).send_keys('A12345678aA')

    def click_button_registr(self):
        return self.find_element(self.LOCATOR_BUTTON_REGISTR).click()

    def get_text(self):
        return self.find_element(self.LOCATOR_ASS_EMAIL).text

    def get_text_enter(self):
        return self.find_element(self.LOCATOR_BUTTON_ENTER).text

    def send_phone(self):
        return self.find_element(self.LOCATOR_EMAIL_PHONE).send_keys('9198902635')

    def send_registr_phone(self):
        return self.find_element(self.LOCATOR_EMAIL_PHONE).send_keys('9857991133')

    def send_7symbol_pass(self):
        return self.find_element(self.LOCATOR_PASSWORD).send_keys('1234567')

    def send_7symbol_double_pass(self):
        return self.find_element(self.LOCATOR_DOUBLE_PASSWORD).send_keys('1234567')

    def get_error_pass(self):
        return self.find_element(self.LOCATOR_ERROR_PASS).text

    def get_error_double_pass(self):
        return self.find_element(self.LOCATOR_ERROR_DOUBLE_PASS).text

    def send_21symbol_pass(self):
        return self.find_element(self.LOCATOR_PASSWORD).send_keys('PaxKt5lmwkBkGdA0oBf2D')

    def send_21symbol_double_pass(self):
        return self.find_element(self.LOCATOR_DOUBLE_PASSWORD).send_keys('PaxKt5lmwkBkGdA0oBf2D')

    def send_20symbol_pass(self):
        return self.find_element(self.LOCATOR_PASSWORD).send_keys('groPkedBIJzvBtK51z8p')

    def send_20symbol_double_pass(self):
        return self.find_element(self.LOCATOR_DOUBLE_PASSWORD).send_keys('groPkedBIJzvBtK51z8p')