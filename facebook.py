"""
from selenium import webdriver
import time

browser = webdriver.Chrome('I:\chromedriver_win32/chromedriver.exe')
browser.get('https://en-gb.facebook.com/')
print(browser.title)
"""
n = int(input("Enter some num:"))
midile_space = 1
leftspace = n-1
for i in range(n):
    if i == 0:
        print(" "*leftspace+'*')
        leftspace -= 1
    elif i == n//2:
        print(" "*leftspace+" ".join(['*']*(i+1)))
        leftspace -= 1
        midile_space += 2
    else:
        print(" "*leftspace+"*"+" "*midile_space+"*")
        leftspace -= 1
        midile_space += 2
