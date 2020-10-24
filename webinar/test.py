from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
#importing for clearning
from selenium.webdriver.common.keys import Keys
#For date and Time
import datetime, threading
from re import sub
from decimal import Decimal


    #driver = webdriver.Chrome('/Users/anushkaagarwal/Downloads/chromedriver') 
    #driver.get("https://instagram.com")
    #sleep(2)
    #from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

def find_cheapest_flight():

    driver.get("https://www.makemytrip.com/flight/search?tripType=O&itinerary=LKO-MAA-20/11/2020&paxType=A-1_C-0_I-0&cabinClass=E&sTime=1603481794457&forwardFlowRequired=true&mpo=&intl=false")
    sleep(12)
    fn=driver.find_elements_by_class_name("airways-name")[0].text
    #print("Cheapest Flight Right Now is " +fn)
    price1= driver.find_elements_by_class_name("actual-price")[0].text
    price = Decimal(sub(r'[^\d.]', '', price1))
    #print("The cost of the flight is"+ price)
    
    return fn, price
  
"""def find_cheapest_flight():
    un= input("Enter Cheap flight name  ")
    up= int(input("Enter New flight price  "))
    return un, up"""

def sendemail():
        

def foo():
    lowest_flight_name=""
    lowest_flight_price=100000000
    updated_name, updated_price= find_cheapest_flight()
    if(updated_price < lowest_flight_price):
        lowest_flight_price= updated_price
        lowest_flight_name= updated_name
        #ALERT function
        sendemail()
    print(lowest_flight_name)
    print(lowest_flight_price)

    
    
    threading.Timer(10, foo).start()

foo()


    
    


    #driver.find_element_by_css_selector("body > main > div > div > div:nth-child(4) > div.leaveIntentBlockOuter.slidein > div > div > span").click()
    #driver.find_element_by_css_selector("#FromSector_show").send_keys("Lucknow")
    #driver.find_element_by_css_selector("#ui-id-19 > span.cty").click()

    
    
 
   
 

  

