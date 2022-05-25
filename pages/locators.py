from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, '.btn-group a[href*="basket"]')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ADDED_SUCCESSFULLY_TO_CART_MESSAGE = (By.CSS_SELECTOR, '#messages :first-child .alertinner strong')
    CART_TOTAL_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-info .alertinner strong')


class CartPageLocators:
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, 'p>a[href^="/"]')
    CART_ITEMS_FORM = (By.CSS_SELECTOR, '.basket-items')
