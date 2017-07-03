''' App Engine Configuration '''
import logging
import os
import sys
from google.appengine.ext import vendor

logging.info("sys platform: " + sys.platform)
logging.info("os name: " + os.name)
logging.info("server software: " + os.environ.get('SERVER_SOFTWARE', ''))

on_appengine = os.environ.get('SERVER_SOFTWARE', '').startswith('Development')# pylint: disable=invalid-name
if on_appengine and os.name == 'nt':
    sys.platform = "Not Windows"

# Add any libraries installed in the "lib" folder.
vendor.add('lib')
