import smtplib
import MySQLdb

passfile = open("password")
password = passfile.read().rstrip()
db=MySQLdb.connect(user="csclub", passwd=password,db="csclubmembers")
c=db.cursor()
c.execute("SELECT email FROM members")
addresses = c.fetchall()


mlist = 'mail@csclub.org.au'
subject = "plantain"
text = "test test test"
message = "Subject: %s\r\n" % subject\
       +"From: %s\r\n" % mlist\
       +"To: %s\r\n" % mlist\
       +"Subject: %s\r\n" % subject\
       +"\r\n" + text
toaddrs = [mlist] + addresses

mailer = smtplib.SMTP('localhost')
mailer.sendmail(mlist, toaddrs, message)
mailer.quit()

