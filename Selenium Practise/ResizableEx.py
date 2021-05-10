from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://jqueryui.com/resources/demos/resizable/default.html")
driver.maximize_window()
driver.implicitly_wait(1)

resizable = driver.find_element_by_xpath("//*[@id=\"resizable\"]/div[3]")

ActionChains(driver).drag_and_drop_by_offset(resizable,400,400).perform()