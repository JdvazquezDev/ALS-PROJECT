# Usuario
from google.appengine.ext import ndb


class Usuario:
  nombre = ndb.StringProperty(required=True)
  email = ndb.StringProperty(required=True)
