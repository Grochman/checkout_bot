from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(executable_path='chromedriver.exe'))
wait = WebDriverWait(driver, 30)

file_path = "links.txt"

n = 0
n_max = 0

with open(file_path, "r") as file:
    for line in file:

        line = line.strip()
        print(line)

        driver.get(line)
        n += 1
        driver.execute_script("window.open();")
        driver.switch_to.window(driver.window_handles[n])
    n -= 1
    n_max = n
    driver.get("https://booksale.pl/login#link_logowanie_PG")


input("start buying: ")
driver.switch_to.window(driver.window_handles[n])
while n >= 0:
    driver.switch_to.window(driver.window_handles[n])
    driver.refresh()
    n -= 1

n = n_max
while n >= 0:
    driver.switch_to.window(driver.window_handles[n])
    link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='product']/div[2]/div[6]/div[2]/a")))
    link.click()
    n -= 1

element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tCart']/a[1]")))
element.click()


time.sleep(2)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='wysylka_1_22']")))
element.click()
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='map-search']")))
element.clear()
element.send_keys("Białkowo")

time.sleep(1)
element.send_keys(Keys.ARROW_DOWN)
element.send_keys(Keys.ENTER)

element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='map-canvas']/div/div/div[2]/div[2]/div/div[3]/div[8]/img")))
element.click()

element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='map-canvas']/div/div/div[2]/div[2]/div/div[4]/div/div/div/div[1]/div/div/div/div[4]/a")))
element.click()


element = driver.find_element(By.XPATH, "//*[@id='rodo']")
element.click()
element = driver.find_element(By.XPATH, "//*[@id='rules']")
element.click()

element = driver.find_element(By.XPATH, "//*[@id='summary']/div[4]/span[2]")
value = element.text
value = value.replace(",", ".")
value = value.replace(" PLN", "")
try:
    cost = float(value)
    if cost >= 80:
        print("free delivery (should buy)")
    else:
        print("no free delivery")
    print("cost:", cost)
except ValueError:
    print("Unable to convert to an integer.")
    print(value)

input("pres key to exit")
driver.quit()
print("proces finished")
