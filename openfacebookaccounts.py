from csv import reader
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from selenium.webdriver.common.keys import Keys
# from pynput.keyboard import   Controller
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait

opt=Options()
opt.add_experimental_option('detach',True)
opt.add_argument("--disable-notifications")
url = 'https://www.facebook.com/jncxindia'

def Connecting_To_Browser(id_str, pass_str):
    if id_str != "" and pass_str != "":
        # driver = webdriver.Chrome(executable_path="C:\\Users\\jc\\Downloads\\chromedriver.exe",options=opt)
        driver = webdriver.Chrome('chromedriver.exe',options=opt)
        try:
            driver.get(url)
            time.sleep(1)

            driver.find_element(By.ID, "login_form").click()

            time.sleep(2)

            driver.find_element(By.ID, "email").click()
            driver.find_element(By.ID, "email").send_keys(id_str)


            time.sleep(1) 

           

            driver.find_element(By.ID, "pass").click()
            driver.find_element(By.ID, "pass").send_keys(pass_str)

            time.sleep(1)

            driver.find_element(By.TAG_NAME, "button").click()
            driver.find_element(By.CSS_SELECTOR, '[name="login"]').click()

            time.sleep(2)

               # driver.quit()
        except:
            # driver.quit()
            time.sleep(1)
    else:               
        print("Either ID or PASSWORD is null") 
        

    


with open('id_pass.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

print("Total Ids and Passwords: ", len(list_of_rows))
total_Len = len(list_of_rows)

ids_pass_list = list_of_rows

for i in range(len(ids_pass_list)):
    id_str = ids_pass_list[i][0]
    id_pass = ids_pass_list[i][1]
    print(i)
    print("Login Id: ", id_str)
    print("Login Password: ", id_pass)

    Connecting_To_Browser(id_str, id_pass)