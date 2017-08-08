''' Settings in datastore '''
from google.appengine.ext import ndb

class Settings(ndb.Model):
    ''' Settings '''
    name = ndb.StringProperty()
    value = ndb.StringProperty()

    @staticmethod
    def get(name):
        ''' get a setting '''
        not_set_value = "NOT SET"
        retval = Settings.query(Settings.name == name).get()
        if not retval:
            retval = Settings()
            retval.name = name
            retval.value = not_set_value
            retval.put()
        if retval.value == not_set_value:
            raise Exception(('Setting %s not found in the database. A placeholder ' +
                             'record has been created. Go to the Developers Console for your app ' +
                             'in App Engine, look up the Settings record with name=%s and enter ' +
                             'its value in that record\'s value field.') % (name, name))
        return retval.value
