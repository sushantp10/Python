from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

#function to close previos tab
def close_last_tab():
    if (len(driver.window_handles) == 2):
        driver.switch_to.window(window_name=driver.window_handles[0])
        driver.close()
        driver.switch_to.window(window_name=driver.window_handles[-1])

test_username = input("Enter your username: ")
test_password = input("Enter you password: ")
test_search = input("Enter name of product you want to search: ")

#Browser Opening
driver = webdriver.Chrome("C:\\Users\\admin\Downloads\\chromedriver.exe")
driver.get("https://www.flipkart.com/")
driver.maximize_window()
wait = ui.WebDriverWait(driver,3)
wait.until(page_is_loaded)

#To cancel login Box and continue search
'''button=driver.find_element_by_xpath("/html/body/div[2]/div/div/button")
   button.click()'''
   
#Login Flipkart Account
sign_id=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
sign_id.send_keys(test_username)
sleep(1)
sign_pass=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")
sign_pass.send_keys(password)
sleep(1)
login=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
sleep(3)

#Product Search
SearchBar=driver.find_element_by_class_name("LM6RPg")
SearchBar.clear()
SearchBar.send_keys(test_search, Keys.ARROW_DOWN)
SearchBar.send_keys(Keys.RETURN)

#Product opening in new tab
product = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME,'_3liAhj'))) #using find by elements we can access any ele under that class
print(product[1].text)                                # here we accessing 2ed product in row
product[1].click()
sleep(2)
close_last_tab()

#adding product to kart
add_kart=driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[1]/div[2]/div/ul/li[1]/button")
add_kart.click()

#Closing Web Browser
sleep(3)
driver.quit()
