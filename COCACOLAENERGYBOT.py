#COCA COLA BOT CHROMEDRIVER BY ARVID for educational purposes only

#Selenium import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import personnummer

import os
from time import sleep
import random


print("COCA COLA BOT CHROMEDRIVER BY ARVID for educational purposes only")
sleep(1)


#Funktionen bot
def bot():
  username_string = "Hej"
  #Öppnar koder.txt
  f = open("koder.txt", "a")

  driver = webdriver.Chrome(executable_path='./chromedriver.exe')
  driver.get('https://coke.studentkortet.se/')


  #Fält för personnummret
  username = driver.find_element_by_id('personal_number')
  username.send_keys(username_string)
  #Knappen för att verifiera personnummret
  nextButton = driver.find_element_by_id('verify_button')
  nextButton.click()


  sleep(3)
  #While loop
  while True:
          try:
            if driver.find_element_by_class_name('number'):
              kod = driver.find_element_by_class_name('number')
              kod=str(kod.text)
              f.write(kod + "\n")
              print("Koden:")
              print(kod)
              f.close()
              driver.close()
              bot()
          except:
              f.close()
              driver.close()
              bot()


#Används för att starta botten när du kör programmet direkt
bot()