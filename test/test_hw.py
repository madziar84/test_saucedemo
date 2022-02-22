import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.basics import Basics
from utils.fields import Fields


class Exercise(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")

        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
        self.driver.get("https://www.saucedemo.com/")

        self.basics = Basics(self.driver)

    def test_saucedemo(self):
        # login to web application
        self.basics.clear_element(Fields.username_textfield)
        self.basics.send_text_to_element(Fields.username_textfield, "standard_user")
        self.basics.clear_element(Fields.username_passwordfield)
        self.basics.send_text_to_element(Fields.username_passwordfield, "secret_sauce")
        self.basics.click_element(Fields.login_button)

        # change sort order from high to low price
        self.basics.click_element(Fields.sort_active_option)

        # add any 3 products to the cart
        self.basics.click_element(Fields.add_to_cart)
        self.basics.click_element(Fields.add_to_cart1)
        self.basics.click_element(Fields.add_to_cart2)

        # navigate to cart
        self.basics.click_element(Fields.shopping_cart)

        # checkout your order
        self.basics.click_element(Fields.checkout_order)

        # fill the data (first, last name and zip code)
        self.basics.send_text_to_element(Fields.first_name, "Magda")
        self.basics.send_text_to_element(Fields.last_name, "B")
        self.basics.send_text_to_element(Fields.postal_code, "01-001")

        # click continue
        self.basics.click_element(Fields.click_continue)

        # calculate the tax value in the code by subtracting item total value from total value
        total_price = self.basics.total_price(Fields.summary_total)
        subtotal_price = self.basics.subtotal_price(Fields.summary_subtotal)
        tax_price = self.basics.tax_price(Fields.summary_tax)
        my_tax = float(total_price) - float(subtotal_price)

        # assertion that expected tax value from web is same as the calculated one
        self.assertAlmostEqual(float(tax_price), my_tax)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
