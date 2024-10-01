from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://google.com")


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)


input_element = driver.find_element(by=By.CLASS_NAME, value="gLFyf")
input_element.clear()

input_element.send_keys("Webcave" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Webcave"))

)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Webcave")
link.click()

time.sleep(5)

driver.quit()