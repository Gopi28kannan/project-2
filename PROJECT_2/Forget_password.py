from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class webpage1:

     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

     def get_url(self):
          #get url
          self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
          #maximize window
          self.driver.maximize_window()

     def forget_password(self):
          wait = WebDriverWait(self.driver, 20)
          #show login page and click forget password process
          try:
               wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[class='orangehrm-login-forgot']"))).click()
               time.sleep(2)
               self.driver.find_element(By.NAME, value="username").send_keys('Admin')
               time.sleep(2)
               self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
               print("forget password and reset password link, successfully completed")
               time.sleep(5)
               #back the webpage two times and show login page 
               self.driver.back()
               time.sleep(2)
               self.driver.back()
          #No such element exception error from forget_password_error
          except  NoSuchElementException as error:
               print('forget_password  error : \n',error)
          
     def shutdown(self):
          time.sleep(8)
          self.driver.quit()

#run this particular  file, please unhide for  command to code
'''web1=webpage1()
web1.get_url()
time.sleep(4)
web1.forget_password()
web1.shutdown()'''
