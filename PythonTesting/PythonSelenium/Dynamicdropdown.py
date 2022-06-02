import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\Sanjana.Math\PycharmProjects\Drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("Ind")
time.sleep(2)
Countries = driver.find_elements_by_xpath("//li[@class='ui-menu-item']/a")
#print(len(Countries))
for Country in Countries:
    if Country.text == "India":
        Country.click()
        break
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"