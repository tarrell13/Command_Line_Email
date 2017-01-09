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
    (2) Sends a message to the recipient

Requirements:

    (1) Accept command line arguments using sys
    (2) Uses smtplib to verify source and recipient
    (3) Uses smtp to send the message to the clientp
    (4) Takes command line string to enter into compose field and then send

Usage: ./commandEmail.py -s source@domain -r recipient@domain -m The Message
Required
-s:         Source Address
-r:         Recipient Address
-m:         Message to Send

NOTES:

Examples:....(1) ./commandEmail.py -s johnny@yahoo.com -t sarah@gmail.com  -m This is a Test
'''

import smtplib
import getpass
import sys
import re
import getopt
import os

commands = ["-s", "-r", "-m"]

source_address = ""
recipient_address = ""
message = ""

'''Prints the usage out to the user'''
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

'''Pattern Matching for Yahoo Address'''
def yahooCheck(address):

    yahoo = re.compile(r"@yahoo.com")
    if re.search(yahoo, address):
        return True
    else:
        return False

def verizonCheck(address):

    verizon = re.compile(r"@verizon.net")
    if re.search(verizon, address):
        return True
    else:
        return False

def comcastCheck(address):

    comcast = re.compile(r"@comcast.net")
    if re.search(comcast, address):
        return True
    else:
        return False


def password():
    pw = getpass.getpass("Enter password for %s: " %source_address)
    return pw

'''Main function will craft the message and send to the client'''
def main():

    options()

    try:
        if verizonCheck(source_address):
            smObj = smtplib.SMTP("smtp.verizon.net", 587)
            smObj.ehlo()
            smObj.starttls()
            smObj.login(source_address, password())
            smObj.sendmail(source_address, recipient_address, message)
        elif gmailCheck(source_address):
            smObj = smtplib.SMTP("smtp.gmail.com", 587)
            smObj.ehlo()
            smObj.starttls()
            smObj.login(source_address, password())
            smObj.sendmail(source_address, recipient_address, message)
        elif yahooCheck(source_address):
            smObj = smtplib.SMTP("smtp.mail.yahoo.com", 587)
            smObj.ehlo()
            smObj.starttls()
            smObj.login(source_address, password())
            smObj.sendmail(source_address, recipient_address, message)
        elif comcastCheck(source_address):
            smObj = smtplib.SMTP("smtp.comcast.net", 587)
            smObj.ehlo()
            smObj.starttls()
            smObj.login(source_address, password())
            smObj.sendmail(source_address, recipient_address, message)

        smObj.quit()
    except:
        print("Invalid")



main()


