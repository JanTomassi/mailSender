import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
head = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comunicazione</title>
    <link rel="stylesheet" href="style.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit&display=swap');

        #header h1 {
            font-weight: 900;
        }

        #header h4 {
            font-weight: 200;
        }

        #wrapper *{
            font-weight: 400;
        }

        #wrapper h1{
            font-weight: 600;
        }

        #wrapper h3{
            font-weight: 600;
        }

        #body {
            margin-right: 10%;
            margin-left: 10%;
        }

        #wrapper {
            display: table;
        }

        .divs {
            display: table-cell;
        }

        #leftdiv {
            width: 75%;
        }

        #rightdiv {
            width: 25%;
        }

        /* For width 400px and larger: */
        @media only screen and (max-width: 25cm) {
            #body {
                margin-right: 0%;
                margin-left: 0%;
            }
        }
    </style>
</head>
'''
body = '''
<div id="body" style="
    font-family: 'Outfit', sans-serif;">
    <div id="header" style="text-align: center; 
        background: rgb(0, 0, 160); 
        width: 100%;
        margin-bottom: 50pt;">
        <h4 style="color: yellow;"><i>La newsletter ufficiale dell'Associazione Ex Alunni Chris Cappell</i></h4>
        <h4 style="color: rgb(175, 175, 175);">{}, NUMERO {}</h4>
        <h1 style="color: white;">{}</h1>
        <h4 style="color: rgb(175, 175, 175);">{}</h4>
    </div>

    <div id="wrapper">

        <div id="leftdiv" class="divs">
            <h1 style="margin-top: 0;">{}</h1>
            {}
        </div>

        <div id="rightdiv" class="divs" style="
            background: rgb(180, 199, 231);
            color: white;
            text-align: center;">
            <h3>{}</h3>
            <h5>- {}</h5>
        </div>

        <div style="content: '';
        display: table;
        clear: both;"></div>
    </div>
    <footer style="background: rgb(0, 0, 160); 
    position: relative; 
    height: 25px;
    width: 100%;"></footer>
</div>

</html>
'''

with open('./Titoli.txt','r') as f:
    lines = f.readlines()
    assert len(lines) == 7, "Numero di righe in Titoli.txt è {} deve essere 7".format(len(lines))
    body = body.format(lines[0][:-1], lines[1][:-1], lines[2][:-1], lines[3][:-1], lines[4][:-1], "{}", lines[5][:-1], lines[6][:-1])

with open('./Contenuto.txt','r') as f:
    bloob = f.read()
    body = body.format(bloob)

mail_content = head+body

#exalunniccc@gmail.com
# List mail, pass, subject, list with \n

#The mail addresses and password
sender_address = ''
sender_pass = ''
receiver_address = ''
subject= ''
#Setup the MIME
message = MIMEMultipart()

with open('./MailConfig.txt', 'r') as f:
    sender_address = f.readline()
    sender_pass = f.readline()
    subject = f.readline()

    mail_addrs = f.readlines()
    for addr in mail_addrs[:-1]:
        receiver_address += addr[:-1]+', '
    receiver_address += mail_addrs[-1]


message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = subject

#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'html'))
print(message)

# Create SMTP session for sending the mail
try:
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
except smtplib.SMTPAuthenticationError as err:
    print(err)
finally:
    input("Wait for input to close ")