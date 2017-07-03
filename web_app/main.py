# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from flask import Flask, render_template, request

# [START create_app]
app = Flask(__name__) # pylint: disable=invalid-name
# [END create_app]

@app.route('/')
def hello():
    return 'Hello World!'

# [START form]
@app.route('/form')
def form():
    return render_template('form.html')
# [END form]


# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():
    email = request.form['email']
    message = request.form['message']

    # [END submitted]
    # [START render_template]
    return render_template(
        'submitted_form.html',
        email=email,
        message=message)
    # [END render_template]


@app.errorhandler(500)
def server_error(error):
    ''' Log any errors and send 500 '''
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request. ' + error.msg)
    return 'An internal error occurred.', 500
# [END app]
