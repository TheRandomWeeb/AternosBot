import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = uc.Chrome()

def TurnOnServer():
    with driver:
        driver.get('https://aternos.org/go/')
    
    if driver.title != "Servers | Aternos | Free Minecraft Server":
        USER = driver.find_element(By.ID, "user")
        PASSWORD = driver.find_element(By.ID, "password")

        USER.send_keys("FunniTestThingy")
        PASSWORD.send_keys("ngothuan12")
        
        time.sleep(5)
        PASSWORD.send_keys(Keys.RETURN)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "server-body"))
        )
        element.click()

        element3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "statuslabel-label"))
        )

        if element3 == "Offline": 
            element2 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "start"))
            )
            element2.click()
    finally:
        pass


def ServerStatus():
    with driver:
        driver.get('https://aternos.org/go/')
    
    if driver.title != "Servers | Aternos | Free Minecraft Server":
        info = ''
        USER = driver.find_element(By.ID, "user")
        PASSWORD = driver.find_element(By.ID, "password")

        USER.send_keys("FunniTestThingy")
        PASSWORD.send_keys("ngothuan12")
        
        time.sleep(5)
        PASSWORD.send_keys(Keys.RETURN)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "server-body"))
        )
        element.click()

        element3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "statuslabel-label"))
        )
        info = element3.text
    finally:
        pass

    return info
