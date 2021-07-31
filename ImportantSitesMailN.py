#https://cryptomaniaks.com/
#WORKS 7/26/2021
# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from datetime import date
import unittest, time, re, os
import timeit
import shutil
import json
import smtplib, ssl #needed for sending email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#####################HEADLESS BROWSER##############################################################S
#options = FirefoxOptions()
#options.add_argument("--headless")
#print ("FirefoxOptions %s" % options)
#browser = webdriver.Firefox(options=options)
#browser.get("https://cryptomaniaks.com/") #CRYPTOMANIAKS
#print ("OPEN HEADLESS BROWSER")
#f.write('OPEN HEADLESS BROWSER \n'
#browser.implicitly_wait(15))
#--------------------------------------------------------------------------------------------------
#FILE/APP INIT######################################################################################
#--------------------------------------------------------------------------------------------------#
f = open('SeleniumIMP.txt', 'w')
print ("OPENING OUTPUT FILE SeleniumIMP.txt")
f.write('OPENING OUTPUT FILE SeleniumIMP.txt \n')
#-----------------------------------------------------------#
path = os.getcwd()
print ("The current working directory is %s" % path)
file_name = "SCREENSHOTSIMP"
completeName = os.path.join(path,file_name)
print(completeName)
print ("The screenshots directory is %s" % completeName)
f.write("The screenshots directory is %s \n" % completeName)
if os.path.isdir('SCREENSHOTSIMP'):
   print ("SCREENSHOTSIMP DIR EXISTS, DELETING & RECREATING")
   shutil.rmtree (completeName)
   os.mkdir(file_name)
else:
   print ("SCREENSHOTSIMP DIR CREATED")
   os.mkdir(file_name)
#-----------------TIMING----------------------------------------------------------------------------- 
start_time = time.time()
print (start_time)
print ("The start time is %s" % start_time)
print("--- %s seconds ---" % (time.time() - start_time))
#f.write('"--- %s seconds ---" % (time.time() - start_time) \n')
#f.write('The start time is %s" % start_time \n')
#DATE & TIME
today = date.today()
now = datetime.now()
d2 = today.strftime("%B %d, %Y")
#d2 = July 26, 2021
# dd/mm/YY H:M:S
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
print("date and time =", dt_string)
f.write("The date & time is %s \n" % dt_string)
#SAMPLE = f.write("--- %s seconds ---" % (time.time() - start_time))
#SAMPLE = f.write("The elapsed time is %s" % (time.time() - start_time))
#----------------------------------------------------------------------------------------------------
#####################HEADLESS BROWSER##############################################################
#options = FirefoxOptions()
#options.add_argument("--headless")
#print ("FirefoxOptions %s" % options)
#browser = webdriver.Firefox(options=options)
#browser.get("https://cryptomaniaks.com") #CRYPTOMANIAKS SITE
#browser.implicitly_wait(20)
#print ("Opening Headless Browser to https://cryptomaniaks.com")
#f.write('Opening Headless Browser to https://cryptomaniaks.com \n')
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot1.png')
#####################ELEMENTS#####################################################################
#----------------------------------------------------------------------------------------------------
#FIREFOX##########################################################################################
browser = webdriver.Firefox()
browser.implicitly_wait(15)
browser.maximize_window()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot1.png')
print ("Firefox Opening Browser")
f.write('Opening Firefox Browser \n')
#CHROME###########################################################################################
#ChromeDriver
#DesiredCapabilities capabilities = DesiredCapabilities.chrome();
#desired_capabilities=DesiredCapabilities.CHROME
#capabilities.setCapability("chrome.verbose", false);
#options = webdriver.ChromeOptions();
#options.add_argument("--start-maximized");
#browser = webdriver.Chrome(options)
#browser = webdriver.Chrome(chrome_options=options)
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot1.png')
#browser = webdriver.Chrome()
#----------------------------------------------------------------------------------------------------
#SEND MAIL########################################################################################
def Send_Mail():
	fromaddr = "scottmaretick51@gmail.com"
	toaddr = "gayle@cryptomaniaks.com"
	#toaddr = "scottmaretick51@gmail.com"
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Important Sites"
	body = "The Important Sites automated checker ran"
	msg.attach(MIMEText(body, 'plain'))
	filename = "SeleniumIMP.txt"
	attachment = open("/Users/scott/Desktop/SeleniumIMP.txt", "rb")
	p = MIMEBase('application', 'octet-stream')
	p.set_payload((attachment).read())
	encoders.encode_base64(p)
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	msg.attach(p)
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(fromaddr, "<PASSWORD>")
	text = msg.as_string()
	s.sendmail(fromaddr, toaddr, text)
	s.quit()
#################################################################################################
browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com") #CRYPTOMANIAKS SITE
print ("Opening Browser to https://cryptomaniaks.com")
f.write('Opening Browser to https://cryptomaniaks.com \n')
time.sleep(15)
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot2.png')
print ("Capturing screenshot cryptomaniaks.com")
f.write('Capturing screenshot cryptomaniaks.com \n')
#----------------------------------------------------------------------------------------------------
browser.implicitly_wait(15)  
browser.get("https://cryptomaniaks.com/latest-cryptocurrency-news/best-crypto-sports-betting-sites")
print ("Navigating to CM Most Valuable & Important Pages #1 site")
f.write('Navigating to CM Most Valuable & Important Pages #1 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot3.png')
print ("Capturing screenshot #1")
f.write('Capturing screenshot #1 \n')

browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/stake-review")
print ("Navigating to CM Most Valuable & Important Pages #2 site")
f.write('Navigating to CM Most Valuable & Important Pages #2 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot4.png')
print ("Capturing screenshot #2")
f.write('Capturing screenshot #2 \n')

browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/latest-cryptocurrency-news/best-crypto-sports-betting-sites")
print ("Navigating to CM Most Valuable & Important Pages #3 site")
f.write('Navigating to CM Most Valuable & Important Pages #3 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot5.png')
print ("Capturing screenshot #3")
f.write('Capturing screenshot #3 \n')

browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/best-bitcoin-casinos")
print ("Navigating to CM Most Valuable & Important Pages #4 site")
f.write('Navigating to CM Most Valuable & Important Pages #4 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot6.png') 
print ("Capturing screenshot #4")
f.write('Capturing screenshot #4 \n')

browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/bitcoin-gambling-sites")
print ("Navigating to CM Most Valuable & Important Pages #5 site")
f.write('Navigating to CM Most Valuable & Important Pages #5 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot7.png') 
print ("Capturing screenshot #5")
f.write('Capturing screenshot #5 \n')

browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/ethereum-casinos")
print ("Navigating to CM Most Valuable & Important Pages #6 site")
f.write('Navigating to CM Most Valuable & Important Pages #6 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot8.png')
print ("Capturing screenshot #6")
f.write('Capturing screenshot #6 \n')

browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/ethereum-gambling-sites")
print ("Navigating to CM Most Valuable & Important Pages #7 site")
f.write('Navigating to CM Most Valuable & Important Pages #7 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot9.png') 
print ("Capturing screenshot #7")
f.write('Capturing screenshot #7 \n')

browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/best-bitcoin-roulette-sites") 
print ("Navigating to CM Most Valuable & Important Pages #8 site")
f.write('Navigating to CM Most Valuable & Important Pages #8 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot10.png')
print ("Capturing screenshot #8")
f.write('Capturing screenshot #8 \n')

browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/best-way-to-buy-bitcoin")
print ("Navigating to CM Most Valuable & Important Pages #9 site")
f.write('Navigating to CM Most Valuable & Important Pages #9 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot11.png')
print ("Capturing screenshot #9")
f.write('Capturing screenshot #9 \n')

browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/best-bitcoin-lending-sites")
print ("Navigating to CM Most Valuable & Important Pages #10 site")
f.write('Navigating to CM Most Valuable & Important Pages #10 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot12.png')
print ("Capturing screenshot #9")
f.write('Capturing screenshot #9 \n')

browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/guides/best-crypto-tools-checklist")
print ("Navigating to CM Most Valuable & Important Pages #11 site")
f.write('Navigating to CM Most Valuable & Important Pages #11 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot13.png')
print ("Capturing screenshot #10")
f.write('Capturing screenshot #10 \n')

browser.implicitly_wait(15)
browser.get("https://cryptomaniaks.com/recommended-websites-tools")
print ("Navigating to CM Most Valuable & Important Pages #12 site")
f.write('Navigating to CM Most Valuable & Important Pages #12 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot14.png')
print ("Capturing screenshot #10")
f.write('Capturing screenshot #10 \n')

browser.get("https://cryptomaniaks.com/best-cryptocurrencies-to-buy")
print ("Navigating to CM Most Valuable & Important Pages #13 site")
f.write('Navigating to CM Most Valuable & Important Pages #13 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot15.png')
print ("Capturing screenshot #11")
f.write('Capturing screenshot #11 \n')

browser.get("https://cryptomaniaks.com/how-much-to-invest-bitcoin")
print ("Navigating to CM Most Valuable & Important Pages #14 site")
f.write('Navigating to CM Most Valuable & Important Pages #14 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot16.png')
print ("Capturing screenshot #12")
f.write('Capturing screenshot #12 \n')

browser.get("https://cryptomaniaks.com/best-bitcoin-poker-sites") 
print ("Navigating to CM Most Valuable & Important Pages #15 site")
f.write('Navigating to CM Most Valuable & Important Pages #15 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot17.png')
print ("Capturing screenshot #13")
f.write('Capturing screenshot #13 \n')

browser.get("https://cryptomaniaks.com/fr/acheter-bitcoin") 
print ("Navigating to CM Most Valuable & Important Pages #16 site")
f.write('Navigating to CM Most Valuable & Important Pages #16 site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot18.png')
print ("Capturing screenshot #14")
f.write('Capturing screenshot #14 \n')

#-----------------GAMBLING--------------------------------------
browser.get("https://cryptomaniaks.com/gambling#") 
print ("Navigating to CRYPTO GAMBLING site")
f.write('Navigating to CRYPTO GAMBLING site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSIMP/ScreenShot19.png')
print ("Capturing screenshot #15")
f.write('Capturing screenshot #15 \n')
#===============================================================
#-----------------TIMING PLUS CLEANUP--------------------------- 
print("--- %s seconds ---" % (time.time() - start_time))
print ("The elapsed time is %s" % (time.time() - start_time))
f.write("--- %s seconds --- \n" % (time.time() - start_time))
f.write("The elapsed time is %s \n" % (time.time() - start_time))
start = timeit.default_timer()
end = timeit.timeit()
#---------------------------------------------------------------
print ("CLOSE FILE")
f.write('CLOSE FILE \n')
f.close()
Send_Mail()
browser.quit()
#--------------------------------------------------------------------------------------------------
