from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

#Opening chrome with facebook
driver = webdriver.Chrome("C:\\Users\\admin\Downloads\\chromedriver.exe")  #give your driver path
web=driver.get("https://www.facebook.com/")
time.sleep(3)          #time to load site
driver.maximize_window()

#enter credentials 
email_sign=driver.find_element_by_id('email')
email_sign.send_keys('your facebook login id')

password=driver.find_element_by_id('pass')
password.send_keys('Your Facebbok password')
password.send_keys(Keys.ENTER)

#Enter search item (optinal)
search=driver.find_element_by_class_name('_1frb')
search.send_keys('search item')
search.send_keys(Keys.ENTER)
