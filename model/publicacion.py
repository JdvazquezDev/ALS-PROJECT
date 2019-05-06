# Publicacion
from google.appengine.ext import ndb


class Publicacion(ndb.Model):
  titulo = ndb.StringProperty(required=True)
  descripcion = ndb.StringProperty(required=True)
  url = ndb.StringProperty()


def create():
  toret = Publicacion()

  toret.titulo = "Titulo"
  toret.descripcion = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Commodi deserunt quis doloribus nostrum excepturi quos porro amet dolor sed similique non exercitationem eveniet qui quas rerum quo error veniam quia, aliquid, culpa nulla? Corrupt ipsum, nesciunt soluta non dignissimos odit placeat cupiditate ducimus natus veniam aliquid id laudantium veritatis impedit!"
  toret.url = "https://source.unsplash.com/1920x1080/?poker,chips,cards"

  return toret


@ndb.transactional
def update(publicacion):
    return publicacion.put()
