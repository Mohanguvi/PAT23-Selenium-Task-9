from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class LoginAutomation:

   def __init__(self, url, username, password): # constructor function for url, username, password, driver
       self.url = url
       self.username = username
       self.password = password
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):  # boot function to access into the website
       self.driver.get(self.url)
       self.driver.maximize_window()
       self.sleep(5)

   @staticmethod
   def sleep(seconds): # function to sleep/idealise the process between each action
       sleep(seconds)

   def inputBox(self, value, key): # function to find the element by ID to get attribute
       self.driver.find_element(By.ID, value).send_keys(key)
       self.sleep(5)

   def submitBtn(self): # function to login
       self.driver.find_element(By.ID, "login-button").click()
       self.sleep(10)

   def fetch_title(self): # function to fetch the title of the webpage once it entered
       return self.driver.title

   def fetch_current_url(self): # function to fetch the current url
       return self.driver.current_url

   def fetch_page_contents(self): # function to enter the contents of the entire page
       return self.driver.page_source

   def save_page_contents_to_file(self, filename): # function to save the file in the .txt format
       with open(filename, "w", encoding="utf-8") as file:
           file.write(self.fetch_page_contents())

   def quit(self): # function to quit once the task is completed
       self.driver.quit()

   def login(self):  # function to login with credentials.
       self.boot()
       self.inputBox("user-name", self.username)
       self.inputBox("password", self.password)
       self.submitBtn()


url = "https://www.saucedemo.com/"
username = "standard_user"    # login username key
password = "secret_sauce"     # password key

obj = LoginAutomation(url, username, password)
obj.boot()    # Call boot function

# Call inputBox function
obj.inputBox("user-name", username)
obj.inputBox("password", password)

# Call submitBtn function
obj.submitBtn()

# Call fetch_title function
title = obj.fetch_title()
print("Title:", title)

# Call fetch_current_url function
current_url = obj.fetch_current_url()
print("Current URL:", current_url)

# Call save_page_contents_to_file function
obj.save_page_contents_to_file("Webpage_task_11.txt")
print("Page contents saved to file: Webpage_task_11.txt")

# Call quit function
obj.quit()