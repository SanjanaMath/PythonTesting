from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome(executable_path="C:\\Users\Sanjana.Math\PycharmProjects\Drivers\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#enter value in text field

driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
ProductsCount = len(driver.find_elements_by_xpath("//div[@class='products-wrapper']//div[@class='product']"))
assert ProductsCount == 3

AddToCart = driver.find_elements_by_xpath("//div[@class='product-action']/button")

AddToCart.click()
