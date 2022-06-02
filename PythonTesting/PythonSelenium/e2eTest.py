from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\Sanjana.Math\PycharmProjects\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]").click()
driver.maximize_window()
driver.find_element(By.XPATH, "//*[contains(text(),'Blackberry')]/parent::h4/parent::div/following-sibling::*//button").click()
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("India")
driver.find_element(By.XPATH, "//div[@class='suggestions']/ul").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
SuccessMsg = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in SuccessMsg
driver.get_screenshot_as_file("Blackberryorder.png")
driver.quit()






