import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request, jsonify
from werkzeug.contrib.fixers import ProxyFix
import json

app = Flask(__name__)

def getAppSetting(key):
   with open('app.config') as f:
      data = json.load(f)
      return data[key]

EMAIL_USERNAME = getAppSetting('emailUsername')
EMAIL_PASSWORD = getAppSetting('emailPassword')
SMTP_SERVER = getAppSetting('smtpServer')
SMTP_PORT = getAppSetting('smtpPort')
SMTP_CREDENTIALS = '{0}:{1}'.format(SMTP_SERVER, SMTP_PORT)


def send_email(to, _from, subject, message):
   msg = "\r\n".join([
     "From: " + _from,
     "To: " + to,
     "Subject: " + subject,
     "",
     message
     ])
   server = smtplib.SMTP(SMTP_CREDENTIALS)
   server.ehlo()
   server.starttls()

   # The account you login into to send the email
   server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
   server.sendmail(_from, to, msg)
   server.quit()


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/linux'):
   return render_template('linux.html')

@app.route('/contact', methods=['POST'])
def contact():
   try:
      name = request.form['name']
      email = request.form['email']
      message = request.form['message']
      data = 'Contact from olafurjohannsson.com, a message from {0} with email {1}\r\n{2}'.format(name, email, message)
      send_email('olafurjohannss@gmail.com', 'olafurjohannss@gmail.com', 'Contact on olafurjohannsson.com', data)
      return jsonify(sendstatus=1)
   except Exception as err:
      return jsonify(sendstatus=0)


app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == '__main__':
   app.run()


