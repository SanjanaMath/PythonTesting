from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


s = Service("C:\\Users\Sanjana.Math\PycharmProjects\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.XPATH, "//div[@class='example']//a").click()
ParentWindow = driver.window_handles[0]
ChildWindow = driver.window_handles[1]
driver.switch_to.window(ChildWindow)
print(driver.find_element(By.XPATH , "//div[@class='example']").text)
driver.switch_to.window(ParentWindow)
print(driver.find_element(By.XPATH , "//div[@class='example']").text)

