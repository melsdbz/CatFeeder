import servoTest
import CatCam
from GmailWrapper import GmailWrapper
import time
from datetime import datetime
import os
from dotenv import load_dotenv

#dotenv for environmental variables
load_dotenv()


#info for picture
now = datetime.now()
date_name = now.strftime("%m-%d-%Y--%H:%M:%S")
filename = "/home/pi/Pictures/CatCam/"+date_name+".jpg"

#info for gmail from environmental variables
IMAP_host = os.getenv("IMAP_host")
IMAP_user = os.getenv("IMAP_user")
IMAP_pass = os.getenv("IMAP_pass")
SMTP_host = os.getenv("SMTP_host")
SMTP_user = os.getenv("SMTP_user")
SMTP_pass = IMAP_pass

def feedByGmail():
    gmailWrapper = GmailWrapper(IMAP_host, SMTP_host, IMAP_user, IMAP_pass, SMTP_user, SMTP_pass)
    ids = gmailWrapper.getIdsBySubject('feed Gigi')
    if(len(ids) > 0):
        try:
            servoTest.feed()
            email_addr = gmailWrapper.getSender(ids)
            gmailWrapper.markAsRead(ids)
            CatCam.takePic(filename)
            time.sleep(4)
            msg = gmailWrapper.createMsg(date_name, SMTP_user, email_addr, filename)
            gmailWrapper.sendMsg(msg)
        except:
            print("Couldn't feed Gigi :/")

if __name__ == '__main__':
    feedByGmail()

