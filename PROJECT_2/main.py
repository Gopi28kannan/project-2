#this file run three python files in current folder, and get the single run option
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
# Test case id 1 run as Forget_pasword
import Forget_password as FP

#Test case id 2 run as Validate_header
import Validate_header as VH

#Test case id 3 run as Validate_menu_list
import Validate_menu_list  as VML
        
def test_1():
     FP.webpage1().get_url()
     FP.webpage1().forget_password()

         
def test_2():
     VH.webpage2().get_url()
     VH.webpage2().login()
     VH.webpage2().validate_admin_page_title()
     print("validate admin page title successfully runned\n")


def test_3():
     VH.webpage2().validate_admin_page_options()
     print("\nvalidate admin page options successfully runned\n")


def test_4():
     VML.webpage3().get_url()
     VML.webpage3().login()
     VML.webpage3().menu_validate()
     print("\n'validate menu list options successfully runned\n")

print("\nAll files runned successfully")
