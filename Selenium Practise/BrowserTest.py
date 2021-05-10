from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#driver = webdriver.Chrome(executable_path="")
#driver = webdriver.Firefox(executable_path="")

'''
Code for upgrading the browser

'''

#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install()) 
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())



driver.get("http://way2automation.com")

driver.maximize_window()

title = driver.title

print(title)

assert "Selenium" in title

driver.close() #Closes the current window where the focus is on

driver.quit() # Quit kills the entire session