from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from dotenv import load_dotenv
from forms import ContactForm
import os

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

@app.route('/contact')
def contact():
    form=ContactForm()
    return render_template('contact.html', form=form)
# --------------------------------------------SERVER RUN-----------------------------------------#
if __name__ == "__main__":
    app.run(host='192.168.68.101', port=5000,debug=True)