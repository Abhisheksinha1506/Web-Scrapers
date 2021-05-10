import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://gmail.com")
driver.maximize_window()
driver.implicitly_wait(10) #waits for the presence of the element
wait = WebDriverWait(driver,10)

driver.find_element_by_id("identifierId").send_keys("username")
driver.find_element_by_xpath("//*[@id=\"identifierNext\"]/div/button/div[2]").click()

element = wait.until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id=\"password\"]/div[1]/div/div[1]/input")))

element.send_keys("ksfbksndfsjkdfj")

driver.find_element_by_xpath("//*[@id=\"passwordNext\"]/div/button/div[2]").click()

error_msg = driver.find_element_by_xpath("//*[@id=\"view_container\"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]/div[2]").text
print(error_msg)