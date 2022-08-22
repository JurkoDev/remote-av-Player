from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

driver.get("http://127.0.0.1:5000/player.html")
sleep(1)
fullscreen_button = driver.find_element(by=By.ID, value="fullscreen")
fullscreen_button.click()

sleep(20)

driver.quit()
