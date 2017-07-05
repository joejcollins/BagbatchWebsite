''' SController for the application '''
import logging
import secrets
import forms
from flask import Flask, flash, render_template, request
from flask_wtf.csrf import CSRFProtect
from google.appengine.api import app_identity # pylint: disable=E0401
from google.appengine.api import mail # pylint: disable=E0401

# Initialize the application with CSRF
app = Flask(__name__) # pylint: disable=invalid-name
app.secret_key = secrets.SECRET_KEY
CSRF = CSRFProtect(app)
CSRF.init_app(app)
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = secrets.RECAPTCHA_PUBLIC_KEY
app.config['RECAPTCHA_PRIVATE_KEY'] = secrets.RECAPTCHA_PRIVATE_KEY
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}

@app.route('/', methods=['GET', 'POST'])
def form():
    ''' Show the message form '''
    message_form = forms.MessageForm()
    if message_form.validate_on_submit():
        return render_template('submitted_form.html', form=message_form)
    return render_template('form.html', title="Message", form=message_form)

def send_mail(their_email, their_message):
    ''' Send an email message '''
    message = mail.EmailMessage(sender=app_identity.get_application_id() +
                                '@appspot.gserviceaccount.com>')
    message.subject = 'Message from Bagbatch Website'
    message.to = secrets.EMAIL
    message.body = """From: {}\n\n<<BEGINS>>\n\n{}\n\n<<ENDS>>""".format(their_email, their_message)
    message.send()

@app.errorhandler(500)
def server_error(error):
    ''' Log any errors and send 500 '''
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request. ' + str(error))
    return 'An internal error occurred.', 500
