import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from urllib.request import urlopen
import urllib
import time
import cv2

while True:
    try:
        urlopen("http://www.google.com").close()
    except urllib.error.URLError:
        print("Not Connected")
        time.sleep(5)
    else:
        print("Connected")
        from_addr = "weatherstationsecure@gmail.com"
        to_addr = "weatherstationsecure@gmail.com"

        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = "WEATHER STATION INTRUSION NOTIFICATION."

        body = "There has been intrusion detected at the weather station"

        msg.attach(MIMEText(body, 'plain'))

        filename = "1.jpg"
        attachment = open("captures/"+filename, "rb")
        ace = type(attachment)
        print(ace)
        #file = "captures/1.jpg"
        #attachment = cv2.imread(file)

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_addr, "W1meaict.")
        text = msg.as_string()
        server.sendmail(from_addr, to_addr, text)
        server.quit()
        '''for filename in mylist:
            part = MIMEApplication(open(filename).read())
            part.add_header('Content-Disposition',
                    'attachment; filename="%s"' % os.path.basename(filename))
            msg.attach(part)'''