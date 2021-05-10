from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def is_element_present(how, what):
    if len(driver.find_elements(by=how, value=what)) == 0:
        return False
    else:
        return True


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("http://www.tizag.com/htmlT/htmlcheckboxes.php")
driver.maximize_window()
driver.implicitly_wait(1)


# i=1

# driver.find_element_by_xpath("//div[4]/input[1]").click()
# driver.find_element_by_xpath("//div[4]/input[2]").click()
# driver.find_element_by_xpath("//div[4]/input[3]").click()
# driver.find_element_by_xpath("//div[4]/input[4]").click()

# while is_element_present(By.XPATH, "//div[4]/input["+str(i)+"]"):
#     driver.find_element_by_xpath("//div[4]/input["+str(i)+"]").click()
#     i += 1
#
# print("Total checkboxes are : ",i-1)
block = driver.find_element_by_xpath("/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/div[4]")
checkboxes = block.find_elements(By.NAME,"sports")

print(len(checkboxes))

for checkbox in checkboxes:
    print("Before clicking : ",checkbox.is_selected())
    checkbox.click()
    print("After clicking : ", checkbox.is_selected())