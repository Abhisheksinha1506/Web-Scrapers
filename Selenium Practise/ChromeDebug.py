from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress","localhost:9222")

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)

#driver.get("http://gmail.com")
#driver.maximize_window()


driver.find_element_by_id("identifierId").send_keys("trainer@way2automation.com")