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

#Function/method to click an empty random square
def move():
    board = driver.find_element(By.CLASS_NAME,'board') #we have to initialize the board in order to find the square in below line
    square = driver.find_elements(By.CSS_SELECTOR,'div.square:not(.x):not(.o)')
        
    if square:
        random_square = random.choice(square)
        random_square.click()
        time.sleep(1)

#Play 10 games
for game in range(10):
#Now we need to keep making moves until the game is over
    while True:
        move()       
        
        try:
            restart = driver.find_element(By.CSS_SELECTOR,'div.restart[style="display: block;"]') #this will make sure we keep playing till the style changes from none to block
            if restart.is_displayed():
                game += 1
                restart_board = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]") #restof the board is blocked by this so we have to click on it to restart
                restart_board.click()
                time.sleep(2)
                move()
                break
        except:
            pass
driver.quit()
