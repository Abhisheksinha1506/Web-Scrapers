from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


chrome_options = Options()


#chrome_options = webdriver.ChromeOptions()

prefs = {"profile.default_content_setting_values.notifications" : 2} #Disable Push Notification on websites
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)

driver.get("http://www.google.com")
driver.maximize_window()

print(driver.title)