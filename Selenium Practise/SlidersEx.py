from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://jqueryui.com/resources/demos/slider/default.html")
driver.maximize_window()
driver.implicitly_wait(1)


mainSlider = driver.find_element_by_id("slider")

location = mainSlider.location
size = mainSlider.size

w,h = size['width'], size['height']

print(location)
print(size)

print(w,h)





slider = driver.find_element_by_xpath("//*[@id=\"slider\"]/span")

ActionChains(driver).drag_and_drop_by_offset(slider,w/2,0).perform()