import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\Sanjana.Math\PycharmProjects\Drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(Checkboxes))

for Checkbox in Checkboxes:
    if Checkbox.get_attribute("value") == "option2":
        Checkbox.click()
        assert Checkbox.is_selected()

Radiobuttons = driver.find_elements_by_name("radioButton")
#print(len(Radiobuttons))
Radiobuttons[2].click()
time.sleep(3)
driver.close()

