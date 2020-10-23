from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


    #driver = webdriver.Chrome('/Users/anushkaagarwal/Downloads/chromedriver') 
    #driver.get("https://instagram.com")
    #sleep(2)
    #from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://instagram.com")



