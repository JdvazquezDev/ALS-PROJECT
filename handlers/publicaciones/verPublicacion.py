
import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2
from google.appengine.ext import ndb
from model.publicacion import Publicacion
import model.usuario as usuario


class VerPublicacionHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    usr_info = usuario.devolver(user)

    if user and usr_info:

      access_link = users.create_logout_url("/")
      try:
        publicacion = ndb.Key(urlsafe=id).get()
      except KeyError:
        self.redirect("/verEntradas")
        return

      template_values = {
        "titulo": Publicacion.titulo,
        "descripcion": Publicacion.descripcion,
        "url": Publicacion.url,
        "publicacion": publicacion,
        "usr_info": usr_info,
        "access_link": access_link
      }

      jinja = jinja2.get_jinja2(app=self.app)
      self.response.write(jinja.render_template("verPublicacion.html", **template_values))
    else:
      self.redirect("/")


app = webapp2.WSGIApplication([
    ("/publicaciones/verPublicacion", VerPublicacionHandler),
  ], debug=True)
