# for facebook 

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://www.facebook.com/'


driver = webdriver.Chrome('chromedriver')
# driver = webdriver.Edge("msedgedriver.exe")
driver.get(url)

time.sleep(1)


               
               
# element = driver.findElement(By.id("UserName")) 
# element.clear(); 

driver.find_element(By.ID, "email").click()
driver.find_element(By.ID, "email").send_keys()


time.sleep(1)

driver.find_element(By.ID, "pass").click()
driver.find_element(By.ID, "pass").send_keys('')

time.sleep(1)

driver.find_element(By.TAG_NAME, "button").click()
driver.find_element(By.CSS_SELECTOR, '[name="login"]').click()

time.sleep(1)

driver.find_element(By.TAG_NAME, "label").click()
# driver.find_element(By.TAG_NAME, "input").send_keys('jncx')

# driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

# # for gmail

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By


# url = 'https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'


# driver = webdriver.Chrome('chromedriver')
# # driver = webdriver.Edge("msedgedriver.exe")
# driver.get(url)

# time.sleep(1)


               
               
# # element = driver.findElement(By.id("UserName")) 
# # element.clear(); 

# driver.find_element(By.ID, "identifierId").click()
# driver.find_element(By.ID, "identifierId").send_keys('ns3329676@gmail.com')

# driver.find_element(By.TAG_NAME, "button").click()

# # time.sleep(1)
# driver.find_element(By.TAG_NAME, "password").click()

# driver.find_element(By.TAG_NAME, "password").send_keys('nitinss123')

# time.sleep(1)

# driver.find_element(By.TAG_NAME, "button").click()
# # driver.find_element(By.CSS_SELECTOR, '[name="login"]').click()

