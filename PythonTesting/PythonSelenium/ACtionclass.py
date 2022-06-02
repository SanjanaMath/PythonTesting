from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#s = Service("C:\\Users\Sanjana.Math\PycharmProjects\Drivers\chromedriver.exe")
#driver = webdriver.Chrome(service=s)
driver = webdriver.Chrome("C:\\Users\Sanjana.Math\PycharmProjects\Drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//div[@class='mouse-hover']")).perform()
action.move_to_element(driver.find_element(By.XPATH, "//div[@class='mouse-hover-content']/a[2]")).click().perform()


