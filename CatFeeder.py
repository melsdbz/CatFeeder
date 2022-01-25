import servoTest
import CatCam
from GmailWrapper import GmailWrapper
import time
from datetime import datetime
import os
from dotenv import load_dotenv, dotenv_values
import twitterBot

#dotenv for environmental variables
load_dotenv()

#info for picture
now = datetime.now()
date_name = now.strftime("%m-%d-%Y--%I:%M%p")
filename = "/home/melsdbz/Pictures/CatCam/"+date_name+".jpg"

#info from environmental variable
IMAP_host = os.getenv("IMAP_host")
IMAP_user = os.getenv("IMAP_user")
IMAP_pass = os.getenv("IMAP_pass")
SMTP_host = os.getenv("SMTP_host")
SMTP_user = os.getenv("SMTP_user")
SMTP_pass = IMAP_pass
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


def feedByGmail():
    en = dotenv_values()
    gmailWrapper = GmailWrapper(IMAP_host, SMTP_host, IMAP_user, IMAP_pass, SMTP_user, SMTP_pass)
    bigFeedIds = gmailWrapper.getIdsBySubject('feed gigi')
    snackIds = gmailWrapper.getIdsBySubject('snack time')
    if(len(bigFeedIds) > 0):
        try:
            servoTest.feed()
            email_addr = gmailWrapper.getSender(bigFeedIds)
            gmailWrapper.markAsRead(bigFeedIds)
            CatCam.takePic(filename)
            time.sleep(4)
            msg = gmailWrapper.createMsg(date_name, SMTP_user, email_addr, filename)
            gmailWrapper.sendMsg(msg)
            if(email_addr in en.keys()):
                newEmailAddr = os.getenv(email_addr)
            else:
                newEmailAddr = email_addr
            twitterBot.tweetPlz(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, newEmailAddr, date_name, filename)
        except:
            print("Couldn't feed Gigi his big meal :/")
          
    if(len(snackIds) > 0):
        try:
            servoTest.feedSnack()
            email_addr = gmailWrapper.getSender(snackIds)
            gmailWrapper.markAsRead(snackIds)
            CatCam.takePic(filename)
            time.sleep(4)
            msg = gmailWrapper.createMsg(date_name, SMTP_user, email_addr, filename)
            gmailWrapper.sendMsg(msg)
            if(email_addr in en.keys()):
                newEmailAddr = os.getenv(email_addr)
            else:
                newEmailAddr = email_addr
            twitterBot.tweetPlzSnack(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, newEmailAddr, date_name, filename)
        except:
            print("Couldn't feed Gigi his snack :/")           

if __name__ == '__main__':
    feedByGmail()

