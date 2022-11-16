import time

from pages.LoginPage import LoginPage
from pages.cart_page import CartPage
from pages.CheckoutOverviewPage import *
from pages.InventoryItemPage import InventoryItemPage
from pages.InventoryPage import InventoryPage
import pytest


@pytest.mark.usefixtures("setup")
class Test:
    def test_main(self):

        product_number = "2"
        login_test = LoginPage(self.driver)
        login_test.authorization('standard_user', 'secret_sauce')

        inventory_test = InventoryPage(self.driver)
        item_title_ip_test = inventory_test.item_title_ip(product_number)
        item_price_ip_test = inventory_test.item_price_ip(product_number)

        inventory_test.find_and_click_item(product_number)

        inventory_item_test = InventoryItemPage(self.driver)

        assert item_title_ip_test == inventory_item_test.item_title_iip()
        assert item_price_ip_test == inventory_item_test.item_price_iip()

        inventory_item_test.add_to_cart()

        cart_test = CartPage(self.driver)

        cart_test.checkout_cart_find_click()
        cart_test.fill_checkout_form()

        checkout_test = CheckoutOverviewPage(self.driver)

        assert checkout_test.finish_item_title() == item_title_ip_test
        assert checkout_test.finish_item_price() == item_price_ip_test

        item_subtotal_price_value = checkout_test.item_subtotal_price()
        tax_price_value = checkout_test.tax_price()
        total_plus_tax_price_value = checkout_test.total_plus_tax_price()

        # assert float(total_plus_tax_price_value) == float(tax_price_value) + float(item_subtotal_price_value)

        checkout_test.click_finish_button()


