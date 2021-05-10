import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("http://www.way2automation.com/")
driver.maximize_window()
driver.implicitly_wait(1)


windows = driver.window_handles

for window in windows:
    print(window)

driver.find_element_by_xpath("//*[@id=\"wrapper\"]/header/div[2]/div/div[2]/div/a[1]").click()

# windows = driver.window_handles
#
# for window in windows:
#     print(window)
#     driver.switch_to.window(window)

driver.switch_to.window(driver.window_handles[1])

driver.find_element_by_id("user_email").send_keys("trainer@way2automation.com")

# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# driver.close()

driver.quit()