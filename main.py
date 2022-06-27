from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from dotenv import load_dotenv
from forms import ContactForm

import smtplib
import os

my_gmail = os.environ.get("GMAIL")
my_password = os.environ.get("APP_PASSWORD")
# --------------------------------------------CONFIGURATION-------------------------------------#
app = Flask(__name__)
load_dotenv("E:\PYTHON_BOOTCAMP_Dr_ANGELA_YU\portfolioproject1\.env")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap(app)

@app.route('/')
def home():
    year = datetime.now().year

    return render_template('index.html', year=year)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/academia')
def academia():
    return render_template('academia.html')

@app.route('/contact', methods=["POST","GET"])
def contact():
    form=ContactForm()
    if form.validate_on_submit():
        email=form.email.data
        name = form.name.data
        message = form.message.data
        phone = form.phone.data
        send_email(name, email, phone, message)
        form.email.data = ""
        form.name.data = ""
        form.message.data = ""
        form.phone.data = ""
        return render_template('contact.html', form=form, msg_sent=True)

    return render_template('contact.html', form=form)
def send_email(name, email, phone , message):
    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()
        connection.login(user=my_gmail, password=my_password)
        connection.sendmail(from_addr=my_gmail,
                            to_addrs="divya4shivalaya@gmail.com",
                            msg=f"Subject:Contact from Portfolio !\n\n"
                                f"Hi this is message from {name}\n"
                                f"say hi\n"
                                f"This is my contact details {phone}, {email}\n"
                                f"{message}"
                            )
# --------------------------------------------SERVER RUN-----------------------------------------#
if __name__ == "__main__":
    app.run(host='192.168.68.111', port=5000,debug=True)