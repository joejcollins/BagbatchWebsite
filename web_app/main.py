''' Controller for the application '''
import logging
import forms
import sys, traceback, os
from models import Settings
from flask import Flask, render_template
from google.appengine.api import app_identity # pylint: disable=E0401
from google.appengine.api import mail # pylint: disable=E0401

# Initialize the application with CSRF
app = Flask(__name__) # pylint: disable=invalid-name
# Set the Flask debug to false so you can use GAE debug
app.config.update(DEBUG = False)
app.secret_key = Settings.get('SECRET_KEY')
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = Settings.get('RECAPTCHA_PUBLIC_KEY')
app.config['RECAPTCHA_PRIVATE_KEY'] = Settings.get('RECAPTCHA_PRIVATE_KEY')
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}

@app.before_request
def enable_local_error_handling():
    ''' test of log  '''
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

@app.route('/', methods=['GET', 'POST'])
def form():
    ''' Show the message form for the user to fill in '''
    message_form = forms.MessageForm()
    if message_form.validate_on_submit():
        send_mail(message_form.email.data, message_form.message.data)
        return render_template('submitted_form.html', title="Thanks", form=message_form)
    return render_template('form.html', title="Message", form=message_form)

def send_mail(their_email, their_message):
    ''' Send an email message to me '''
    message = mail.EmailMessage(sender=app_identity.get_application_id() +
                                '@appspot.gserviceaccount.com>')
    message.subject = 'Message from Bagbatch Website'
    message.to = Settings.get('EMAIL')
    message.body = """From: {}\n\n<<BEGINS>>\n\n{}\n\n<<ENDS>>""".format(their_email, their_message)
    message.send()

@app.errorhandler(500)
def server_error(error):
    ''' Log any errors to the browser because you are too lazy to look at the console

    The Flask DEBUG setting must the set to false for this to work '''
    exception_type, exception_value, trace_back = sys.exc_info()
    no_limit = None
    exception = ''.join(traceback.format_exception(exception_type, exception_value,
                                                   trace_back, no_limit))
    logging.exception('An error occurred during a request. ' + str(error))
    return render_template('500.html', title=error, exception=exception)
