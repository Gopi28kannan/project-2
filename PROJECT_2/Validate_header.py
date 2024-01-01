from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class webpage2:
     
     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

     def get_url(self):
          #get url
          self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
          #maximize window
          self.driver.maximize_window()
          

     def login(self):
          # still wait upto 20 seconds
          wait = WebDriverWait(self.driver, 20)
          #try method use login process
          try:
               #still wait visibility of element located
               wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'))).send_keys('Admin')
               time.sleep(2)
               self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')
               time.sleep(2)
               submit_button = self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
               print("logged in successfully")
          #no such element exception from login errors
          except NoSuchElementException as selenium_error:
               print("login errors ;\n",selenium_error)

     def validate_admin_page_title(self):
          wait = WebDriverWait(self.driver, 20)
          #validate admin page title and validate admin page options and display output console
          try:
               wait.until(EC.visibility_of_element_located((By.XPATH,'//span[text()="Admin"]'))).click()
               time.sleep(3)
               #print admin page title in output console
               print("Admin page title : ",self.driver.title,'\n')
          except NoSuchElementExcetion as error:
               print('validate_admin_page_title',error)

     def validate_admin_page_options(self):
          wait = WebDriverWait(self.driver, 20)
          try:
               #go to admin
               wait.until(EC.visibility_of_element_located((By.XPATH,'//span[text()="Admin"]'))).click()
               time.sleep(3)
               #collect admin page options use via xpath
               Admin_validate=self.driver.find_elements(By.XPATH,'//header//div//nav//ul//li')
               admin_xpath_count = len(Admin_validate)
               time.sleep(3)
               #suppose visible more option at display, in header list last.  And then first click more option and  count elements 
               more_option_xpath = self.driver.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]//span[text()="More "]')
               more_count = len(more_option_xpath)
               if more_count == 1:
                    for element in more_option_xpath:
                         element.click()
                         time.sleep(1)
                         visible_more_options = self.driver.find_elements(By.XPATH,'//div//nav//ul//li//ul//div')
                         visible_more1_options = len(visible_more_options)
               else:
                    visible_more1_options = 0
               print("validate the options are displaying on this Admin page :")
               count=1
               #use loop highlight and move header admin page options one by one, and print options in output console
               for element in Admin_validate:
                    highlight = ActionChains(self.driver)
                    highlight.move_to_element(element).perform()
                    if visible_more1_options == 0: 
                         print(element.text)
                         time.sleep(1)
                    else:
                         if admin_xpath_count != count:
                              print(element.text)
                              time.sleep(1)
                              #click more option
                         if  admin_xpath_count == count:
                              element.click()
                              time.sleep(2)
                    count=count+1
               #suppose more options display in admin page options at last, already click more option and visible next elements
               #suppose more option not display in admin page options at last, just skip this loop lines automatically
               if more_count == 1:
                    for element in visible_more_options:
                         highlight = ActionChains(self.driver)
                         highlight.move_to_element(element).perform()
                         print(element.text)
                         time.sleep(1)
          #No such element exception from validate_admin_page
          except NosuchElementException as error:
               print("validate_admin_page errors : \n",error)

     def shutdown(self):
          time.sleep(4)
          self.driver.quit()

#run this particular  file, please unhide for  command to code   
'''web2 = webpage2()
web2.get_url()
web2.login()
web2.validate_admin_page_title()
#web2.validate_admin_page_options()
web2.shutdown()'''
