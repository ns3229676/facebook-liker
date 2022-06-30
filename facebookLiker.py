# for facebook 

# from pynput.keyboard import  Controller
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By

# url = 'https://www.facebook.com/'

# driver = webdriver.Chrome('chromedriver')

# driver.get(url)

# time.sleep(1)

# driver.find_element(By.ID, "email").click()
# driver.find_element(By.ID, "email").send_keys('nitinsaxena1819@gmail.com')


# time.sleep(1)

# driver.find_element(By.ID, "pass").click()
# driver.find_element(By.ID, "pass").send_keys('7078990406n')

# time.sleep(1)

# driver.find_element(By.TAG_NAME, "button").click()
# driver.find_element(By.CSS_SELECTOR, '[name="login"]').click()

# time.sleep(3)

# driver.get('https://www.youtube.com/channel/UCp0aUP9U8MQ3rNcUOz1YjuA')






# from pynput.keyboard import  Controller
# import time
# from selenium import webdriver
# import csv
# from csv import reader
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service

# keyboard = Controller()

# def Connecting_To_Browser(id_str, pass_str):
#     if id_str != "" and pass_str != "":

#         s=Service('C:\\Users\\jc\\Downloads\\chromedriver.exe')
#         browser=webdriver.Chrome(service=s)
        
#         # browser.get('https://www.facebook.com/')
#         browser.get('https://www.facebook.com/jncxindia')
#         time.sleep(1)

#         keyboard.press('j')
#         keyboard.release('j')

#         keyboard.press('j')
#         keyboard.release('j')

        






#         # browser.find_element(By.CLASS_NAME, " rq0escxv l9j0dhe7 du4w35lb j83agx80 rj1gh0hx buofh1pr g5gj957u hpfvmrgz taijpn5t bp9cbjyn owycx6da btwxx1t3 d1544ag0 tw6a2znq jb3vyjys dlv3wnog rl04r1d5 mysgfdmx hddg9phg qu8okrzs g0qnabr5").click()

#         # keyboard.press('l')
#         # keyboard.release('l')

#         # browser.find_element(By.ID, "email").click()
#         # browser.find_element(By.ID, "email").send_keys('nitinsaxena1819@gmail.com')

#         # time.sleep(1)

       

#         # browser.find_element(By.ID, "pass").click()
#         # browser.find_element(By.ID, "pass").send_keys('7078990406n')

#         # time.sleep(1)

#         # browser.find_element(By.TAG_NAME, "button").click()
#         # browser.find_element(By.CSS_SELECTOR, '[name="login"]').click()

#         # time.sleep(3)

#         # browser.navigate().refresh()
        

       


            
        

#         time.sleep(10)
#         # browser.quit()

#     else:
#         print("Either ID or PASSWORD is null")

    
#     # browser.get('https://www.facebook.com/jncxindia')

# with open('id_pass.csv', 'r') as read_obj:
#     # pass the file object to reader() to get the reader object
#     csv_reader = reader(read_obj)
#     # Pass reader object to list() to get a list of lists
#     list_of_rows = list(csv_reader)

# print("Total Ids and Passwords: ", len(list_of_rows))
# total_Len = len(list_of_rows)

# ids_pass_list = list_of_rows

# for i in range(len(ids_pass_list)):
#     id_str = ids_pass_list[i][0]
#     id_pass = ids_pass_list[i][1]
#     print(i)
#     print("Login Id: ", id_str)
#     print("Login Password: ", id_pass)

#     Connecting_To_Browser(id_str, id_pass)







import keyboard
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import   Controller
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



opt=Options()
# opt.add_experimental_option("debuggerAddress","localhost:8989")
# driver=webdriver.Chrome(executable_path="C:\\Users\\jc\\Downloads\\chromedriver.exe",chrome_options=opt)

# opt.add_argument("--disable-infobars")
# opt.add_argument("start-maximized")
# opt.add_argument("--disable-extensions")
opt.add_argument("--disable-notifications")

# Pass the argument 1 to allow and 2 to block




keyboard = Controller()

s=Service('C:\\Users\\jc\\Downloads\\chromedriver.exe')
# driver=webdriver.Chrome(service=s)

driver = webdriver.Chrome(
    executable_path="C:\\Users\\jc\\Downloads\\chromedriver.exe",chrome_options=opt
)
url = 'https://www.facebook.com/jncxindia'

actions = ActionChains(driver) 

driver.get(url)

time.sleep(1)

driver.find_element(By.ID, "login_form").click()

time.sleep(2)



driver.find_element(By.ID, "email").click()
driver.find_element(By.ID, "email").send_keys('')


time.sleep(1)

driver.find_element(By.ID, "pass").click()
driver.find_element(By.ID, "pass").send_keys('')

time.sleep(1)

driver.find_element(By.TAG_NAME, "button").click()
driver.find_element(By.CSS_SELECTOR, '[name="login"]').click()

time.sleep(5)

# opt.add_experimental_option(
#     "prefs", {"profile.default_content_setting_values.notifications": 1}
# )

# keyboard.write('j',delay=0)
pyautogui.press('j',presses=1)


time.sleep(5)

# keyboard.press('j')
# keyboard.release('j')

# # time.sleep(1)

# keyboard.press('l')
# keyboard.release('l')









# option = Options()

# option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
# option.add_argument("--disable-extensions")

# # Pass the argument 1 to allow and 2 to block
# option.add_experimental_option(
#     "prefs", {"profile.default_content_setting_values.notifications": 1}
# )

# driver = webdriver.Chrome(
#     chrome_options=option, executable_path="path-of-driver\chromedriver.exe"
# )
# driver.get("https://www.facebook.com")