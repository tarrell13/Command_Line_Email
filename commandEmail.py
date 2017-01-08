#!/usr/local/bin/python3

'''
Program Name: Command Line Emailer

Write a program that takes an email address and string of text on the command
line and then, using Selenium, logs into your email account and
sends an email of the string to the provided address. (You might want to set
up a separate email account for this program.)

This would be a nice way to add a notification feature to your programs.
You could also write a similar program to send messages from a Facebook
or Twitter account.

Functionality:

    (1) Take in command line arguments
    (2) Logs into email account using username and password
    (3) Sends a message to the recipient

Requirements:

    (1) Accept command line arguments using sys
    (2) Finds appropriate username and password field tags to log in using webdriver
    (3) Uses webdriver to select compose message field
    (4) Takes command line string to enter into compose field and then send

Usage: ./commandEmail.py -s source@domain -r recipient@domain -m The Message
Required
-s:         Source Address
-r:         Recipient Address
-m:         Message to Send

NOTES:

    (1) Be sure to add browser driver to path of browser you want to use. Such as
    browser = webdriver.Chrome(), this method will check PATH for chromedriver

Examples:....(1) ./commandEmail.py -s johnny@yahoo.com -t sarah@gmail.com  -m This is a Test
'''

from selenium import webdriver
import sys
import re
import getopt
import os

commands = ["-s", "-r", "-m"]

source_address = ""
recipient_address = ""
message = ""

def usage():
    print("Usage:  ./commandEmail.py -s source@domain -r recipient@domain -m <Message to Compose>")
    print("Required:")
    print("-s:      Source Address")
    print("-r:      Recipient Address")
    print("-m:      Message to Send")
    print("")
    print("Examples:....(1) ./commandEmail.py -s johnny@yhaoo.com -r sarah@gmailcom -m This is a test message")
    sys.exit()

'''Gather program required options'''
def options():

    global source_address, recipient_address, message

    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:r:m")
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for opt, arg in opts:
        if opt == "-s":
            source_address = arg
        elif opt == "-r":
            recipient_address = arg
        elif opt == "-m":
            message = " ".join(args)

'''Pattern Matching for Gmail Address'''
def gmailCheck(address):

    gmail = re.compile(r"@gmail")

    if re.search(gmail, address):
        return True
    else:
        return False

'''Pattern Matching for Verizon Address'''
def verizonCheck(address):

    verizon = re.compile(r"@verizon.net")
    if re.search(verizon, address):
        return True
    else:
        return False

'''Pattern Matching for Yahoo Address'''
def yahooCheck(address):

    yahoo = re.compile(r"@yahoo.com")
    if re.search(yahoo, address):
        return True
    else:
        return False


def gmailPage(data, recAddress):

    url = "https://mail.google.com/mail/u/0/#inbox"
    browser = webdriver.Chrome()
    browser.get(url)

    # Locate Compose button
    compose_element = browser.find_element_by_class_name("T-I J-J5-Ji T-I-KE L3")
    compose_element.submit()

    # Put Recipient and Message into Compose Field and Send


options()


