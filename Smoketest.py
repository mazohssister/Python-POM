from CartPage import CartPage
from CheckoutOverviewPage import *
from LoginPage import *
from BaseTest import *
from InventoryItemPage import *


class Smoketest:

    def smoketest(self):
        print("Hey, input a number 1-6")
        product_number = input()

        test = BaseTest()
        login_page = LoginPage(test.driver)
        login_page.authorization(test_login_value="standard_user", test_password_value="secret_sauce")

        inventory_test = InventoryPage(test.driver)
        item_title_ip_test = inventory_test.item_title_ip(product_number)
        item_price_ip_test = inventory_test.item_price_ip(product_number)

        inventory_test.find_and_click_item(product_number)

        inventory_item_test = InventoryItemPage(test.driver)

        assert item_title_ip_test == inventory_item_test.item_title_iip()
        assert item_price_ip_test == inventory_item_test.item_price_iip()

        inventory_item_test.add_to_cart()

        cart_test = CartPage(test.driver)

        cart_test.checkout_cart_find_click()
        cart_test.fill_checkout_form()

        checkout_test = CheckoutOverviewPage(test.driver)

        assert checkout_test.finish_item_title() == item_title_ip_test
        assert checkout_test.finish_item_price() == item_price_ip_test

        item_subtotal_price_value = checkout_test.item_subtotal_price()
        tax_price_value = checkout_test.tax_price()
        total_plus_tax_price_value = checkout_test.total_plus_tax_price()

        assert float(total_plus_tax_price_value) == float(tax_price_value) + float(item_subtotal_price_value)

        checkout_test.click_finish_button()

testik = Smoketest()
testik.smoketest()
