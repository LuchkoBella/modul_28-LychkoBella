from selenium.webdriver.common.by import By
# from pages.base_page import BasePage


class LocatorAuthorization:

    URL_MAIN_PAGE = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id' \
                        '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type' \
                        '=code&scope=openid&state=0c88a06a-b30f-4576-879b-b7bbbb0b36d1&theme&auth_type'
    LOCATOR_REGISTRATION = (By.ID, 'kc-register')
    LOCATOR_AUTH_PHONE = (By.ID, 't-btn-tab-phone')
    LOCATOR_AUTH_EMAIL = (By.ID, 't-btn-tab-mail')
    LOCATOR_AUTH_LOGIN = (By.ID, 't-btn-tab-login')
    LOCATOR_AUTH_LS = (By.ID, 't-btn-tab-ls')
    LOCATOR_MESSAGE_MAIL = (By.CSS_SELECTOR, 'span[class="rt-input__placeholder"]')
    LOCATOR_FIELD_USER_NAME = (By.ID, 'username')
    LOCATOR_FIELD_PASSWORD = (By.ID, 'password')
    LOCATOR_BUTTON_ENTER = (By.ID, 'kc-login')
    LOCATOR_LOGOUT = (By.ID, 'logout-btn')
    LOCATOR_ERROR_AUTH = (By.ID, 'form-error-message')
    LOCATOR_FORGOT_PASSWORD = (By.ID, 'forgot_password')
    LOCATOR_GO_TO_BACK = (By.ID, 'reset-back')
    LOCATOR_PRIVACY_POLICY = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]')
    LOCATOR_PUBLIC_OFFER = (By.XPATH, '//*[@id="title"]/h1')
    LOCATOR_BUTTON_VK = (By.ID, 'oidc_vk')
    LOCATOR_VK = (By.XPATH, '/html/body/div/div/div/div[2]/div')
    LOCATOR_SHOW_PASS = (By.CSS_SELECTOR, 'svg[class="rt-base-icon rt-base-icon--'
                                          'fill-path rt-eye-icon rt-input__eye rt-input__eye"]')
    LOCATOR_ASS_SHOW_PASS = (By.CSS_SELECTOR, 'input[id="password"][type="text"] ')
    LOCATOR_BUTTON_OK= (By.ID, 'oidc_ok')
    LOCATOR_BUTTON_MM = (By.ID, 'oidc_mail')
    LOCATOR_BUTTON_GOOGLE = (By.ID, 'oidc_google')
    LOCATOR_BUTTON_YANDEX = (By.ID, 'oidc_ya')


class LocatorRegistration:

    LOCATOR_NAME = (By.CSS_SELECTOR, '[name="firstName"]')
    LOCATOR_LAST_NAME = (By.CSS_SELECTOR, '[name="lastName"]')
    LOCATOR_EMAIL_PHONE = (By.ID, 'address')
    LOCATOR_PASSWORD = (By.ID, 'password')
    LOCATOR_DOUBLE_PASSWORD = (By.ID, 'password-confirm')
    LOCATOR_BUTTON_REGISTR = (By.NAME, 'register')
    LOCATOR_ASS_EMAIL = (By.CSS_SELECTOR, 'h1[class="card-container__title"]')
    LOCATOR_BUTTON_ENTER = (By.NAME, 'gotoLogin')
    LOCATOR_ERROR_PASS = (By.XPATH,
                          '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    LOCATOR_ERROR_DOUBLE_PASS = (By.XPATH,
                                 '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')