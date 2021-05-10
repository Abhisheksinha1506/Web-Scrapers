from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.w3schools.com/")
driver.maximize_window()
driver.implicitly_wait(1)

print(driver.find_element_by_xpath("//*[@id=\"mySidenav\"]/div/a[2]").value_of_css_property("font-size"))

print(driver.find_element_by_xpath("//*[@id=\"mySidenav\"]/div/a[2]").value_of_css_property("color"))

print(driver.find_element_by_xpath("//*[@id=\"mySidenav\"]/div/a[2]").value_of_css_property("font-family"))