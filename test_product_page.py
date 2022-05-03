from pages.productPage import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_be_correct_added_to_cart_success_message()
    page.should_be_correct_cart_total_message()
