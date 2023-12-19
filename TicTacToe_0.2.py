#Author: Ouzer Shema
#We are trying to automate https://playtictactoe.org/ inspired by Angie Jones & EvilTester on youtube
#The objective is to create a bot that engages in 10 games with another game bot, with the primary goal of confirming the playability of these 10 games.

#Importing directories
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

#Initialize web driver
driver = webdriver.Chrome()

#Go to https://playtictactoe.org/
url = "https://playtictactoe.org/"
driver.get(url)

#To initiate game we will first make a random move from all available empty squares
board = driver.find_element(By.CLASS_NAME,'board') #we have to initialize the board in order to find the square in below line
square = driver.find_elements(By.CSS_SELECTOR,'div.square:not(.x):not(.o)')
random_square = random.choice(square)
random_square.click()
time.sleep(1)

#Now we need to keep making moves until the game is over
while True:
    square = driver.find_elements(By.CSS_SELECTOR,'div.square:not(.x):not(.o)')
    
    if square:
        random_square = random.choice(square)
        random_square.click()
        time.sleep(1)
    
    try:
        restart = driver.find_element(By.CSS_SELECTOR,'div.restart[style="display: block;"]') #this will make sure we keep playing till the style changes from none to block
        if restart.is_displayed():
            print("Game over")
            break
    except:
        pass

    