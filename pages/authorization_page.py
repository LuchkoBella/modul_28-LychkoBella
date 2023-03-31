from pages.locator_page import LocatorAuthorization
from pages.base_page import BasePage


class Authorization(BasePage, LocatorAuthorization):

    def click_to_registration(self):
        return self.find_element(self.LOCATOR_REGISTRATION).click()

    def click_to_way_email(self):
        return self.find_element(self.LOCATOR_AUTH_EMAIL).click()

    def click_to_way_login(self):
        return self.find_element(self.LOCATOR_AUTH_LOGIN).click()

    def click_to_way_ls(self):
        return self.find_element(self.LOCATOR_AUTH_LS).click()

    def click_to_way_phone(self):
        return self.find_element(self.LOCATOR_AUTH_PHONE).click()

    def get_text_field_username(self):
        return self.find_element(self.LOCATOR_MESSAGE_MAIL).text

    def send_phone(self):
        return self.find_element(self.LOCATOR_FIELD_USER_NAME).send_keys('9857991133')

    def send_password(self):
        return self.find_element(self.LOCATOR_FIELD_PASSWORD).send_keys('Q12345678qQ')

    def click_button_enter(self):
        return self.find_element(self.LOCATOR_BUTTON_ENTER).click()

    def get_logout(self):
        return self.find_element(self.LOCATOR_LOGOUT)

    def send_invalid_password(self):
        return self.find_element(self.LOCATOR_FIELD_PASSWORD).send_keys('S12345678sS')

    def get_text_error_message_auth(self):
        return self.find_element(self.LOCATOR_ERROR_AUTH).text

    def send_email(self):
        return self.find_element(self.LOCATOR_FIELD_USER_NAME).send_keys('xo4yshe4ka@yandex.ru')

    def click_forgot_password(self):
        return self.find_element(self.LOCATOR_FORGOT_PASSWORD).click()

    def get_button_go_back(self):
        return self.find_element(self.LOCATOR_GO_TO_BACK)

    def click_privacy_policy(self):
        return self.find_element(self.LOCATOR_PRIVACY_POLICY).click()

    def get_public_offer(self):
        return self.find_element(self.LOCATOR_PUBLIC_OFFER).text

    def click_button_vk(self):
        return self.find_element(self.LOCATOR_BUTTON_VK).click()

    def click_button_ok(self):
        return self.find_element(self.LOCATOR_BUTTON_OK).click()

    def click_button_mm(self):
        return self.find_element(self.LOCATOR_BUTTON_MM).click()

    def click_button_google(self):
        return self.find_element(self.LOCATOR_BUTTON_GOOGLE).click()

    def click_button_yandex(self):
        return self.find_element(self.LOCATOR_BUTTON_YANDEX).click()

    def click_show_pass(self):
        return self.find_element(self.LOCATOR_SHOW_PASS).click()

    def get_sow_pass(self):
        return self.find_element(self.LOCATOR_ASS_SHOW_PASS)
