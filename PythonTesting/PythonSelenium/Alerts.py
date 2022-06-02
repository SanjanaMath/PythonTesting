from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\Sanjana.Math\PycharmProjects\Drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
i = alert.text
assert "Hello" in i
alert.dismiss()
alert.accept()

