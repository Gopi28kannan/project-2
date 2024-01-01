from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class webpage3:

     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

     def get_url(self):
          #get url
          self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
          #maximize window
          self.driver.maximize_window()

     def login(self):
          wait = WebDriverWait(self.driver, 20)
          #find username, password and send keys, and click login button
          try:
               wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'))).send_keys('Admin')
               time.sleep(2)
               self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')
               time.sleep(2)
               self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
               print("logged in successfully")
          #No such element exception error from login
          except NoSuchElementException as selenium_error:
               print("login errors ;\n",selenium_error)

     def menu_validate(self):
          #catch menu list and validate of display menu names in output console
          try:
               self.driver.implicitly_wait(10)
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

#run this particular  file, please unhide for  command to code         
'''web3=webpage3()
web3.get_url()
time.sleep(4)
web3.login()
time.sleep(4)
web3.menu_validate()
web3.shutdown()'''
