
#Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def personnummer():
    #Start nummer
    startnmr = "040613"

    #Öppna Personnmr Sida
    driver=webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.get("https://johan.nicklason.se/personnummergenerator/")

    #välj låda skriv nummer o press enter
    username = driver.find_element_by_name('number')
    username.send_keys(startnmr)
    driver.find_element_by_name("number").send_keys(Keys.ENTER)

    #Kopiera personnummer och gör om texten

    nmr = driver.find_element_by_xpath("""//*[@id="home"]/div/p[1]/b""").text

    nmrnobind = nmr.replace('-', '')

    username_string = ("20" + (nmrnobind))

    return(username_string)
