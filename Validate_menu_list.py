from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class webpage3:
     def __init__(self,url):
          self.url = url
          self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

     def get_url(self):
          #get url
          self.driver.get(self.url)
          #maximize window
          self.driver.maximize_window()

     def login(self):
          #find username, password and send keys, and click login button
          try:
               self.driver.find_element(By.NAME, value="username").send_keys('Admin')
               time.sleep(2)
               self.driver.find_element(By.NAME, value="password").send_keys('admin123')
               time.sleep(2)
               self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
               print("logged in successfully")
          #No such element exception error from login
          except NoSuchElementException as selenium_error:
               print("login errors ;\n",selenium_error)

     def menu_validate(self):
          #catch menu list and validate of display menu names in output console
          try:
               menu_list = self.driver.find_elements(By.XPATH,"//aside//nav//div//ul//li//a//span")
               print("validate the menu options are displaying on this Admin page : \n")
               count = 1
               #use for loop
               for element in menu_list:
                    #skip claim option , and not mention this, in the project. So I use if condition
                    if count !=11:
                         # highlight and move the menu names one by one
                         highlight = ActionChains(self.driver)
                         highlight.move_to_element(element).perform()    
                         print(element.text)
                         time.sleep(2)
                    count=count+1
          #No such element exception error from menu_validate
          except NoSuchElementException as error:
               print("menu_validate errors ;\n", error)

     def shutdown(self):
          time.sleep(8)
          self.driver.quit()

url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'          
web3=webpage3(url)
web3.get_url()
time.sleep(4)
web3.login()
time.sleep(4)
web3.menu_validate()
web3.shutdown()
