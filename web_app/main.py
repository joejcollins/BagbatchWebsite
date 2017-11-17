''' Controller for the application '''
import logging
import sys
import traceback
import forms
from models import Settings
from flask import Flask, render_template
from google.appengine.api import app_identity # pylint: disable=E0401
from google.appengine.api import mail # pylint: disable=E0401
from google.appengine.api import users
import pdb

# Initialize the application with CSRF
app = Flask(__name__) # pylint: disable=invalid-name

####################
#### blueprints ####
####################
 
from home.views import users_blueprint
from admin.views import recipes_blueprint
 
# register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(recipes_blueprint)



# Set the Flask debug to false so you can use GAE debug
app.config.update(DEBUG=False)
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

@app.route('/admin', methods=['GET'])
def admin_page():
    ''' Authentication required page '''
    user = users.get_current_user()
    return render_template('admin.html', email=user.email())
