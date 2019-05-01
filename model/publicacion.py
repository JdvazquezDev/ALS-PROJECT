# Publicacion
from google.appengine.ext import ndb


class Publicacion:
  titulo = ndb.StringProperty(required=True)
  descripcion = ndb.StringProperty(required=True)
  url = ndb.StringProperty()


def create():
  toret = Publicacion()

  toret.titulo = "Titulo"
  toret.descripcion = "Contenido principal"
  toret.url = "https://unsplash.com/photos/GikVY_KS9vQ"

  return toret


@ndb.transactional
def update(publicacion):
    return publicacion.put()
