from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

#firefox_options = Options()


#chrome_options = webdriver.ChromeOptions()
firefox_options = webdriver.FirefoxOptions()
firefox_options.set_preference("dom.webnotifications.enabled",False) #Disable Push Notification on websites
firefox_options.headless = True
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=firefox_options)

driver.get("https://www.google.in")
driver.maximize_window()

print(driver.title)