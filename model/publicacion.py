# Publicación
from google.appengine.ext import ndb


class Publicacion:
  titulo = ndb.StringProperty(required=True)
  descripcion = ndb.StringProperty(required=True)
  url = ndb.StringProperty()
