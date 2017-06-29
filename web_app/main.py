import os
import logging

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World of Flask!'

app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]