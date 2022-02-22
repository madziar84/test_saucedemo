from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basics:
    def __init__(self, driver):
        self.local_driver: webdriver.Chrome = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 5)

    def get_element_text(self, element):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        return self.local_driver.find_element(By.XPATH, element).text

    def clear_element(self, element):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        self.local_driver.find_element(By.XPATH, element).clear()

    def send_text_to_element(self, element, text):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        self.local_driver.find_element(By.XPATH, element).send_keys(text)

    def click_element(self, element):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        self.local_driver.find_element(By.XPATH, element).click()

    def total_price(self, element):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        return self.local_driver.find_element(By.XPATH, element).text.replace("Total: $", "")

    def subtotal_price(self, element):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        return self.local_driver.find_element(By.XPATH, element).text.replace("Item total: $", "")

    def tax_price(self, element):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        return self.local_driver.find_element(By.XPATH, element).text.replace("Tax: $", "")
