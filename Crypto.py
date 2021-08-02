#UPDATED 08/01/2021
#INCLUDES NAV BAR
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
#####################HEADLESS BROWSER##############################################################
#options = FirefoxOptions()
#options.add_argument("--headless")
#print ("FirefoxOptions %s" % options)
#browser = webdriver.Firefox(options=options)
#browser.get("https://cryptomaniaks.com/") #CRYPTOMANIAKS
#print ("OPEN HEADLESS BROWSER")
#f.write('OPEN HEADLESS BROWSER \n')
#--------------------------------------------------------------------------------------------------
#FILE/APP INIT######################################################################################
#----------------------------------------------#
f = open('SeleniumCRYPTO.txt', 'w')
print ("OPENING OUTPUT FILE SeleniumCRYPTO.txt")
f.write('OPENING OUTPUT FILE SeleniumCRYPTO.txt \n')
#--------------------------------------------------------------------------------------------------#
path = os.getcwd()
print ("The current working directory is %s" % path)
file_name = "SCREENSHOTSCM"
completeName = os.path.join(path,file_name)
print(completeName)
print ("The screenshots directory is %s" % completeName)
f.write('The screenshots directory is %s" % completeName \n')
#------CHECK FOR EXISTING SCREENSHOTSCM DIR------#
if os.path.isdir('SCREENSHOTSCM'):
   print ("SCREENSHOTSCM DIR EXISTS")
   #os.rmdir(file_name)
   shutil. rmtree (completeName)
   print ("DELETING SCREENSHOTSCM DIR")
   os.mkdir(file_name)
else:
   print ("SCREENSHOTSCM DIR CREATED")
   os.mkdir(file_name)
#----------------------------------------------------------------------------------------------------
#-----------------TIMING----------------------------------------------------------------------------- 
start_time = time.time()
print (start_time)
print ("The start time is %s" % start_time)
print("--- %s seconds ---" % (time.time() - start_time))
f.write('"--- %s seconds ---" % (time.time() - start_time) \n')
f.write('The start time is %s" % start_time \n')
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
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCMP/ScreenShot1.png')
#####################ELEMENTS#####################################################################
#----------------------------------------------------------------------------------------------------
#CSS SELECTOR browser.find_element_by_css_selector("").click()
#
#XPATH #browser.find_element_by_xpath("").click()
#----------------------------------------------------------------------------------------------------
#Scroll to top of page (GO)
#browser.execute_script("window.scrollTo(0, 0);")   #SCROLL TO TOP OF PAGE
#time.sleep(5)
#browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTSCMP/ScreenShot.png');
#FIREFOX##########################################################################################
browser = webdriver.Firefox()
browser.maximize_window()
#CHROME###########################################################################################
#ChromeDriver
#DesiredCapabilities capabilities = DesiredCapabilities.chrome();
#desired_capabilities=DesiredCapabilities.CHROME
#capabilities.setCapability("chrome.verbose", false);
#options = webdriver.ChromeOptions();
#options.add_argument("--start-maximized");
#browser = webdriver.Chrome(chrome_options=options)
#browser = webdriver.Chrome()
#----------------------------------------------------------------------------------------------------  
browser.get("https://cryptomaniaks.com") #CRYPTOMANIAKS SITE
print ("Opening Browser to https://cryptomaniaks.com")
f.write('Opening Browser to https://cryptomaniaks.com \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot1.png')
#NAV BAR#############################################################################################
#EDUCATION
def Education():
	browser.get("https://cryptomaniaks.com") #CRYPTOMANIAKS SITE
	browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(1) > span:nth-child(1)").click()
	print ("Navigating to Education on top of CryptoManiaks site")
#INVEST
def Invest():
	browser.get("https://cryptomaniaks.com") #CRYPTOMANIAKS SITE
	browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(2) > span:nth-child(1)").click()
	print ("Navigating to Invest on top of CryptoManiaks site")
#GAMBLE
def Gamble():
	browser.get("https://cryptomaniaks.com") #CRYPTOMANIAKS SITE
	browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(4) > span:nth-child(1)").click()
	print ("Navigating to Gamble on top of CryptoManiaks site")
#DEFI
def DeFi():
	browser.get("https://cryptomaniaks.com") #CRYPTOMANIAKS SITE
	browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(3) > span:nth-child(1)").click()
	print ("Navigating to DeFi on CryptoManiaks site")
#NFT
def NFT():
	browser.get("https://cryptomaniaks.com") #CRYPTOMANIAKS SITE
	browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(5) > span:nth-child(1)").click()
	print ("Navigating to NFT on top of CryptoManiaks site")
#####################################################################################################
#SEND MAIL###########################################################################################
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
	s.login(fromaddr, "Sm110751$")
	text = msg.as_string()
	s.sendmail(fromaddr, toaddr, text)
	s.quit()
####################################################################################################
#EDUCATION
#browser.find_element_by_xpath("/html/body/div[1]/header/div/div/div[2]/div/nav/ul/li[1]/span").click() #EDUCATION
#browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(1) > span:nth-child(1)").click()
Education()
print ("Navigating to Education on top of CryptoManiaks site")
f.write('Navigating to Education on top of CryptoManiaks site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot2.png')
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(1) > span:nth-child(1)").click() #EDUCATION
#------------------------------------------------------------------------------
#WHAT IS BITCOIN
Education()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)").click()
print ("Navigating to WHAT IS BITCOIN")
f.write('Navigating to WHAT IS BITCOIN \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot3.png')
browser.back() #CRYPTOMANIAKS HOME
#------------------------------------------------------------------------------
#HOW TO INVEST IN BITCOIN
Education()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)").click()
print ("Navigating to WHAT IS BITCOIN")
f.write('Navigating to WHAT IS BITCOIN \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot4.png')
browser.back() #CRYPTOMANIAKS HOME
#------------------------------------------------------------------------------
#HOW TO MAKE MONEY WITH BITCOIN
Education()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)").click()
print ("Navigating to WHAT IS BITCOIN")
f.write('Navigating to WHAT IS BITCOIN \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot5.png')
browser.back() #CRYPTOMANIAKS HOME
#------------------------------------------------------------------------------
#BEST CRYPTO TOOLS
Education()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)").click()
print ("Navigating to WHAT IS BITCOIN")
f.write('Navigating to WHAT IS BITCOIN \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot6.png')
browser.back() #CRYPTOMANIAKS HOME
#------------------------------------------------------------------------------
#50 MISTAKES TO AVOID
Education()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(5) > a:nth-child(1)").click()
print ("Navigating to WHAT IS BITCOIN")
f.write('Navigating to WHAT IS BITCOIN \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot7.png')
browser.back() #CRYPTOMANIAKS HOME
#------------------------------------------------------------------------------
#CRYPTO GLOSSARY
Education()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(6) > a:nth-child(1)").click()
print ("Navigating to WHAT IS BITCOIN")
f.write('Navigating to WHAT IS BITCOIN \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot8.png')
browser.back() #CRYPTOMANIAKS HOME
###########################################################################################################################
#INVEST
#browser.find_element_by_xpath("/html/body/div[1]/header/div/div/div[2]/div/nav/ul/li[2]/span").click() #INVEST
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(2) > span:nth-child(1)").click()
Invest()
print ("Navigating to Invest on top of CryptoManiaks site")
f.write('Navigating to Invest on top of CryptoManiaks site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot9.png')
#--------------------------------------------------------------------------------------------------
#BEST WAYS TO BUY BITCOIN
Invest()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)").click()
print ("Navigating to BEST WAYS TO BUY BITCOIN")
f.write('Navigating to BEST WAYS TO BUY BITCOIN \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot10.png')
browser.back()

#HOW MUCH TO INVEST IN BITCOIN
Invest()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)").click()
print ("Navigating to HOW MUCH TO INVEST IN BITCOIN")
f.write('Navigating to HOW MUCH TO INVEST IN BITCOIN \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot11.png')
browser.back()

#SHOULD I INVEST IN BITCOIN
Invest()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)").click()
print ("Navigating to SHOULD I INVEST IN BITCOIN")
f.write('Navigating to SHOULD I INVEST IN BITCOIN \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot12.png')
browser.back()

#SHOULD I INVEST IN ETHEREUM
Invest()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)").click()
print ("Navigating to INVEST IN ETHEREUM")
f.write('Navigating to INVEST IN ETHEREUM \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot13.png')
browser.back()

#BEST CRYPTOCURRENCIES TO BUY
Invest()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(5) > a:nth-child(1)").click()
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot14.png')
browser.back()
###########################################################################################################################
#DEFI
#browser.find_element_by_xpath("/html/body/div[1]/header/div/div/div[2]/div/nav/ul/li[3]/span").click()
DeFi()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(3) > span:nth-child(1)").click()
print ("Navigating to DeFi on top of CryptoManiaks site")
f.write('Navigating to DeFi on top of CryptoManiaks site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot15.png')
browser.back()

#BEST BITCOIN LENDING SITES
DeFi()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)").click()
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot16.png')
browser.back()

#BEST BITCOIN LOAN SITES
DeFi()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)").click()
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot17.png')
browser.back()

#BEST BITCOIN DEBIT CARDS
DeFi()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)").click()
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot18.png')
browser.back()
###########################################################################################################################
#GAMBLE

Gamble()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(4) > span:nth-child(1)").click()
print ("Navigating to Gamble on top of CryptoManiaks site")
f.write('Navigating to Gamble on top of CryptoManiaks site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot19.png')

#CRYPTO BETTING SITES
Gamble()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)").click()
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot20.png')
browser.back()

#BITCOIN CASINOS
Gamble()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)").click()
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot21.png')
browser.back()

#BITCOIN GAMBLING
Gamble()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)").click()
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot22.png')
browser.back()

#OLYMPICS CRYPTO BETTING
Gamble()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)").click()
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot23.png')
browser.back()

#ETHEREUM GAMBLING SITES
Gamble()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(5) > a:nth-child(1)").click()
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot24.png')
browser.back()

#ETHEREUM CASINOS
Gamble()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(6) > a:nth-child(1)").click()
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot25.png')
browser.back()

#ETHEREUM BETTING SITES
Gamble()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(7) > a:nth-child(1)").click()
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot26.png')
browser.back()

#STAKE.COM REVIEW
Gamble()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(8) > a:nth-child(1)").click()
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot27.png')
browser.back()

#BETONLINE
Gamble()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > a:nth-child(1)").click()
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot28.png')
browser.back()

#BLACK CHIP POKER
Gamble()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > a:nth-child(1)").click()
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot29.png')
browser.back()

#COINPOKER
Gamble()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)").click()
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot30.png')
browser.back()

###########################################################################################################################
#NFT
#browser.find_element_by_xpath("/html/body/div[1]/header/div/div/div[2]/div/nav/ul/li[5]/span").click()
browser.find_element_by_css_selector(".header-nav__menu > li:nth-child(5) > span:nth-child(1)").click()
print ("Navigating to NFT on top of CryptoManiaks site")
f.write('Navigating to NFT on top of CryptoManiaks site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot31.png')

#OPENSEA
NFT()
# .header-nav__menu > li:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot32.png')
browser.back()

#SORARE
NFT()
# .header-nav__menu > li:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)
print ("Navigating to BEST CRYPTOCURRENCIES TO BUY")
f.write('Navigating to BEST CRYPTOCURRENCIES TO BUY \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot33.png')
browser.back()

###########################################################################################################################
#browser.find_element_by_xpath("/html/body/div[1]/header/div/div/div[2]/div/div/a/span").click() #BEST CRYPTO TOOLS
browser.find_element_by_css_selector(".header__cta > a:nth-child(1)").click()
print ("Navigating to Tools on top of CryptoManiaks site")
f.write('Navigating to Tools on top of CryptoManiaks site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot34.png')

#browser.find_element_by_xpath("/html/body/div[1]/header/div/div/div[3]/div/div").click() #FLAG (PREFERENCES)
browser.find_element_by_css_selector(".flag-wrapper > img:nth-child(1)").click()
print ("Navigating to PREFERENCES on top of CryptoManiaks site")
f.write('Navigating to PREFERENCES on top of CryptoManiaks site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot35.png')
# CSS SELECTOR CLICK button.btn
browser.find_element_by_css_selector("button.btn").click()
#time.sleep(5)
print ("SAVING PREFERENCES")
f.write('SAVING PREFERENCES \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot36.png')
#time.sleep(15)
#browser.back() #BACK TO HOME PAGE
browser.get("https://cryptomaniaks.com") #BACK TO HOME PAGE

#browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/ul/li[1]/a/h4").click() #EDUCATION
browser.find_element_by_css_selector(".item-nav--yellow > h4:nth-child(2)").click()
print ("Navigating to Education on CryptoManiaks site")
f.write('Navigating to Education on CryptoManiaks site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot37.png')
browser.back()

#browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/ul/li[2]/a/h4").click() #EXCHANGES
browser.find_element_by_css_selector(".item-nav--violet > h4:nth-child(2)").click()
print ("Navigating to Exchanges on CryptoManiaks site")
f.write('Navigating to Exchanges on CryptoManiaks site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot38.png')
browser.back()

#browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/ul/li[3]/a/h4").click() #DEFI
browser.find_element_by_css_selector(".item-nav--blue > h4:nth-child(2)").click()
print ("Navigating to DeFi on CryptoManiaks site")
f.write('Navigating to DeFi on CryptoManiaks site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot39.png')
browser.back()

#browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/ul/li[4]/a/h4").click() #GAMBLING
browser.find_element_by_css_selector(".item-nav--green > h4:nth-child(2)").click()
print ("Navigating to Gambling on CryptoManiaks site")
f.write('Navigating to Gambling on CryptoManiaks site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot40.png')
browser.back()
#SCROLL TO BOTTOM------------------------------------------------------------------------------
browser.execute_script("window.scrollTo(0, window.scrollY + 4800)")
print ("SCROLLING TO BOTTOM")
f.write('SCROLLING TO BOTTOM \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot41.png')
#----------------------------------------------------------------------------------------------
#Best Resources
#Best Ways To Buy Bitcoin
browser.find_element_by_css_selector("div.footer__top__links:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)").click()
print ("Navigating to Best Ways To Buy Bitcoin")
f.write('Navigating to Best Ways To Buy Bitcoin \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot42.png')
browser.back()

#Blockchain For Dummies
browser.find_element_by_css_selector("div.footer__top__links:nth-child(1) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)").click()
print ("Navigating to Blockchain For Dummies")
f.write('Navigating to Blockchain For Dummies \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot43.png')
browser.back()

#Best Crypto Betting Sites
browser.find_element_by_css_selector("div.footer__top__links:nth-child(1) > ul:nth-child(2) > li:nth-child(3) > a:nth-child(1)").click()
print ("Navigating to Best Ways To Buy Bitcoin")
f.write('Navigating to Best Ways To Buy Bitcoin site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot44.png')
browser.back()

#Best Crypto Lending Sites
browser.find_element_by_css_selector("div.footer__top__links:nth-child(1) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)").click()
print ("Navigating to Best Crypto Lending Sites")
f.write('Navigating to Best Crypto Lending Sites \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot45.png')
browser.back()

#50 Investment Strategy Tips
browser.find_element_by_css_selector("div.footer__top__links:nth-child(1) > ul:nth-child(2) > li:nth-child(5) > a:nth-child(1)").click()
print ("Navigating to 50 Investment Strategy Tips")
f.write('Navigating to 50 Investment Strategy Tips \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot46.png')
browser.back()
#----------------------------------------------------------------------------------------------
#Useful Links
#About
browser.find_element_by_css_selector("div.footer__top__links:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)").click()
print ("Navigating to About")
f.write('Navigating to About \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot47.png')
browser.back()

#Infographics
browser.find_element_by_css_selector("div.footer__top__links:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)").click()
print ("Navigating to Infographics")
f.write('Navigating to Infographics \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot48.png')
browser.back()

#Crypto Guides
browser.find_element_by_css_selector("div.footer__top__links:nth-child(2) > ul:nth-child(2) > li:nth-child(3) > a:nth-child(1)").click()
print ("Navigating to Crypto Guides")
f.write('Navigating to Crypto Guides \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot49.png')
browser.back()

#Best Crypto Products
browser.find_element_by_css_selector("div.footer__top__links:nth-child(2) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)").click()
print ("Navigating to Best Crypto Products")
f.write('Navigating to Best Crypto Products site \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot50.png')
browser.back()

#Contact Us
browser.find_element_by_css_selector("div.footer__top__links:nth-child(2) > ul:nth-child(2) > li:nth-child(5) > a:nth-child(1)").click()
print ("Navigating to Contact Us")
f.write('Navigating to Contact Us \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot51.png')
browser.back()

#Facebook
browser.find_element_by_css_selector(".list-sc > li:nth-child(1) > a:nth-child(1)").click()
time.sleep(10)
print ("Navigating to Facebook")
f.write('Navigating to Facebook \n')
browser.switch_to.window(browser.window_handles[1])
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot52.png')

#Instagram
browser.switch_to.window(browser.window_handles[0])
browser.find_element_by_css_selector(".list-sc > li:nth-child(2) > a:nth-child(1)").click()
time.sleep(10)
print ("Navigating to Instagram")
f.write('Navigating to Instagram \n')
browser.switch_to.window(browser.window_handles[1])
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot53.png')

#Twitter
browser.switch_to.window(browser.window_handles[0])
browser.find_element_by_css_selector(".list-sc > li:nth-child(3) > a:nth-child(1)").click()
time.sleep(10)
print ("Navigating to Twitter")
f.write('Navigating to Twitter \n')
browser.switch_to.window(browser.window_handles[1])
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot54.png')

#LinkedIn
browser.switch_to.window(browser.window_handles[0])
browser.find_element_by_css_selector(".list-sc > li:nth-child(4) > a:nth-child(1)").click()
time.sleep(10)
print ("Navigating to LinkedIn")
f.write('Navigating to LinkedIn \n')
browser.switch_to.window(browser.window_handles[1])
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot55.png')

#mail
#browserC = webdriver.Chrome()
#browserC.get("https://cryptomaniaks.com") #CRYPTOMANIAKS SITE
#browserC.execute_script("window.scrollTo(0, window.scrollY + 800)")
#browserC.switch_to.window(browser.window_handles[0])
#CSS SELECTOR .list-sc > li:nth-child(5) > a:nth-child(1)
#browser.find_element_by_css_selector(".list-sc > li:nth-child(5) > a:nth-child(1)").click()
#XPATH /html/body/div[1]/footer/div/div[1]/div/div/div[1]/div[3]/ul/li[5]/a

#browserC.find_element_by_XPATH("//*[@id="block-block-68"]/div/div/div[1]/div[3]/ul/li[5]/a
#browserC.find_element_by_css_selector("#block-block-68 > div > div > div.col-6-12.col-sm-full.footer__top__left > #div.footer__sc > ul > li:nth-child(5) > a").click()
#time.sleep(10)
#print ("Navigating to mail")
#f.write('Navigating to mail \n')
#browser.switch_to.window(browser.window_handles[1])
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/ScreenShot56.png')

#CryptoManiaks Website-----------------------------------------------------------------------
browser.get("https://cryptomaniaks.com") #CRYPTOMANIAKS SITE
f.write('Opening CryptoManiaks website \n')
print ("Navigating to CryptoManiaks website")
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/screenshot57.png')
time.sleep(5)
#Scroll down #1------------------------------------------------------------------------------
browser.execute_script("window.scrollTo(0, window.scrollY + 600)")
f.write('Scrolling down 1 page \n')
print ("Paging down CryptoManiaks website")
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/screenshot58.png')
time.sleep(5)
#Scroll down #2------------------------------------------------------------------------------
browser.execute_script("window.scrollTo(0, window.scrollY + 600)")
f.write('Scrolling down 1 page \n')
print ("Paging down CryptoManiaks website")
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/screenshot59.png')
time.sleep(5)
#Scroll down #3------------------------------------------------------------------------------
browser.execute_script("window.scrollTo(0, window.scrollY + 600)")
f.write('Scrolling down 1 page \n')
print ("Paging down CryptoManiaks website")
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/screenshot60.png')
time.sleep(5)
#Scroll down #4------------------------------------------------------------------------------
browser.execute_script("window.scrollTo(0, window.scrollY + 800)")
f.write('Scrolling down 1 page \n')
print ("Paging down CryptoManiaks website")
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/screenshot61.png')
time.sleep(5)
#Scroll down #5------------------------------------------------------------------------------
browser.execute_script("window.scrollTo(0, window.scrollY + 600)")
f.write('Scrolling down 1 page \n')
print ("Paging down CryptoManiaks website")
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/screenshot62.png')
time.sleep(5)
#Scroll down #6------------------------------------------------------------------------------
browser.execute_script("window.scrollTo(0, window.scrollY + 800)")
f.write('Scrolling down 1 page \n')
print ("Paging down CryptoManiaks website")
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/screenshot63.png')
time.sleep(5)
#Scroll down #7------------------------------------------------------------------------------
browser.execute_script("window.scrollTo(0, window.scrollY + 600)")
f.write('Scrolling down 1 page \n')
print ("Paging down CryptoManiaks website")
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/screenshot64.png')
time.sleep(5)
#-----------------------------FOOTER-----------------------------------------------------------
#Disclaimer
browser.find_element_by_css_selector(".footer__bottom__list > li:nth-child(1) > a:nth-child(1)").click()
f.write('Navigating to Disclaimer on CryptoManiaks website \n')
print ("Navigating to Disclaimer on CryptoManiaks website")
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/screenshot65.png')
browser.back()

#Terms of Use
browser.find_element_by_css_selector(".footer__bottom__list > li:nth-child(2) > a:nth-child(1)").click()
f.write('Navigating to Terms of Use on CryptoManiaks website \n')
print ("Navigating to Terms of Use on CryptoManiaks website")
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/screenshot66.png')
browser.back()

#Terms of Service
browser.find_element_by_css_selector(".footer__bottom__list > li:nth-child(3) > a:nth-child(1)").click()
f.write('Navigating to Terms of Service on CryptoManiaks website \n')
print ("Navigating to Terms of Service on CryptoManiaks website")
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/screenshot67.png')
browser.back()

#Copyright Notice
browser.find_element_by_css_selector(".footer__bottom__list > li:nth-child(4) > a:nth-child(1)").click()
f.write('Navigating to Copyright Notice on CryptoManiaks website \n')
print ("Navigating to Copyright Notice on CryptoManiaks website")
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/screenshot68.png')
browser.back()

#Privacy policy
browser.find_element_by_css_selector(".footer__bottom__list > li:nth-child(5) > a:nth-child(1)").click()
f.write('Navigating to Privacy policy on CryptoManiaks website \n')
print ("Navigating to Privacy policy on CryptoManiaks website")
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTSCM/screenshot69.png')
browser.back()

#-----------------TIMING PLUS CLEANUP--------------------------- 
print("--- %s seconds ---" % (time.time() - start_time))
print ("The elapsed time is %s" % (time.time() - start_time))
f.write("--- %s seconds ---" % (time.time() - start_time))
f.write("The elapsed time is %s" % (time.time() - start_time))
start = timeit.default_timer()
end = timeit.timeit()
#---------------------------------------------------------------
print ("CLOSE FILE")
f.write('CLOSE FILE \n')
f.close()
browser.quit()
#--------------------------------------------------------------------------------------------------
