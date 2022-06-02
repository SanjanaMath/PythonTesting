from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\Sanjana.Math\PycharmProjects\Drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
driver.find_element_by_name("name").send_keys("rahul")
driver.find_element_by_id("exampleCheck1").click()

print("Done step8")



driver.close()
