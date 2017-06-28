import os
import jinja2

wsgi_config = {}
wsgi_config['webapp2_extras.sessions'] = {
    'secret_key': 'something-very-very-secret',
}

'''
Remember on the App Engine slashes go / not \, but if you are developing on Windows \ will work,
so it can be confusing sometimes.
'''
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/views'),
                                       extensions=['jinja2.ext.autoescape'])