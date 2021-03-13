link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_product_has_add_to_cart_button(browser):
    browser.get(link)
    add_button = browser.find_element_by_class_name('btn-add-to-basket')
    #  проверка, что страница товара на сайте содержит кнопку добавления в корзину
    assert add_button is not None