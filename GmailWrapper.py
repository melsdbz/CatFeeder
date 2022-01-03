from imapclient import IMAPClient, SEEN
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

SEEN_FLAG = 'SEEN'
UNSEEN_FLAG = 'UNSEEN'

class GmailWrapper:
    def __init__(self, IMAP_host, SMTP_host, IMAP_user, IMAP_pass, SMTP_user, SMTP_pass):
        self.IMAP_host = IMAP_host
        self.IMAP_user = IMAP_user
        self.IMAP_pass = IMAP_pass
        self.SMTP_host = SMTP_host
        self.SMTP_user = SMTP_user
        self.SMTP_pass = SMTP_pass
        self.login_IMAP()
        self.login_SMTP()
        
        
    def login_IMAP(self):
        print("Logging in IMAP as: " +self.IMAP_user)
        server = IMAPClient(self.IMAP_host, use_uid=True,ssl=True)
        server.login(self.IMAP_user, self.IMAP_pass)
        self.server = server
    
    def login_SMTP(self):
        print("logging in SMTP as: "+self.SMTP_user)
        server2 = smtplib.SMTP_SSL(self.SMTP_host,465)
        server2.ehlo()
        server2.login(self.SMTP_user,self.SMTP_pass)
        self.server2 = server2
        
    def getIdsBySubject(self, subject, unreadOnly=True, folder="INBOX"):
        self.setFolder(folder)
        self.searchCriteria = [UNSEEN_FLAG, 'SUBJECT', subject]
    
        if(unreadOnly==False):
            self.searchCriteria.append(SEEN_FLAG)
        return self.server.search(self.searchCriteria)
        
    def markAsRead(self, mailIds, folder = "INBOX"):
        self.setFolder(folder)
        self.server.set_flags(mailIds, [SEEN])
    
    def setFolder(self, folder):
        self.server.select_folder(folder)
    
    def getSender(self, ids):
        if len(ids)>0:
            for mail_id, data in self.server.fetch(ids, ['ENVELOPE']).items():
                env = data[b'ENVELOPE']
        #decoding address
        data = env[3][0]

        send_user = data[2].decode("utf-8")
        send_host = data[3].decode("utf-8")
        email_addr = send_user+"@"+send_host
        return email_addr
    
    def createMsg(self, datetime, from_email, to_email, file):
        msg = MIMEMultipart()
        msg["Subject"] = "Cat has been fed at "+datetime
        msg["From"] = from_email
        msg["To"] = to_email
        with open(file, "rb") as fp:
            img = MIMEImage(fp.read())
            img.add_header('Content-Disposition','attachment',filename = "Proof.jpg")
            msg.attach(img)
        return msg
    
    def sendMsg(self, msg):
        self.server2.send_message(msg)
        print("message sent!")
    

        