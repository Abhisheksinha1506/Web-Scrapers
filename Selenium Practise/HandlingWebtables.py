from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.espncricinfo.com/series/a20-league-2020-21-1255254/points-table-standings")
driver.maximize_window()
driver.implicitly_wait(1)

rows = driver.find_elements_by_xpath("//tbody/tr")
total_rows = len(rows)

cols = driver.find_elements_by_xpath("//tbody/tr[1]/td")
total_cols = len(cols)

print("Total rows are : ", total_rows, " and total cols are : ", total_cols)

for row in rows:
    print(row.text)

print("-----Second Way--------")

start_xpath = "//tbody/tr["
mid_xpath = "]/td["
end_xpath = "]"


for row in range(1, total_rows + 1):
    for col in range(1, total_cols + 1):
        print(driver.find_element_by_xpath(start_xpath + str(row) + mid_xpath + str(col) + end_xpath).text, end=" ")
    print()
