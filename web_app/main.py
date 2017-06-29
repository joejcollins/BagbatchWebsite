''' Application Content '''
# [START app]
import logging

# [START imports]
from flask import Flask, render_template, request
# [END imports]

# [START create_app]
APP = Flask(__name__)
# [END create_app]

# [START form]
@APP.route('/contact')
def form():
    ''' Render the form '''
    return render_template('contact.html')
# [END form]


# [START submitted]
@APP.route('/submitted', methods=['POST'])
def submitted_form():
    ''' Handle the posted form '''
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    # [END submitted]
    # [START render_template]
    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)
    # [END render_template]


@APP.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]