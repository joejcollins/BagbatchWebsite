''' main application '''
import json
import logging
import secrets
from flask import Flask, render_template, request
from google.appengine.api import app_identity # pylint: disable=E0401
from google.appengine.api import mail # pylint: disable=E0401

app = Flask(__name__) # pylint: disable=invalid-name

@app.route('/')
def form():
    ''' Show the message form '''
    return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    ''' Respond to the message submission '''
    their_email = request.form['email']
    their_message = request.form['message']
    send_mail(their_email, their_message) # Send
    return render_template(
        'submitted_form.html',
        email=their_email,
        message=their_message)

def send_mail(their_email, their_message):
    ''' Send an email message '''
    message = mail.EmailMessage(sender=app_identity.get_application_id() +
                                '@appspot.gserviceaccount.com>')
    message.subject = 'Message from Bagbatch Website'
    message.to = secrets.EMAIL
    message.body = """From: {}

<<BEGINS>>

{}

<<ENDS>>""".format(their_email, their_message)
    message.send()

@app.errorhandler(500)
def server_error(error):
    ''' Log any errors and send 500 '''
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request. ' + error)
    return 'An internal error occurred.', 500
