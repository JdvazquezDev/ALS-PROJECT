import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from webapp2_extras import jinja2

import model.usuario as usuario
import model.publicacion as publicaciones
from model.publicacion import Publicacion


class ModificarPublicacion(webapp2.RequestHandler):
  def get(self):
    try:
      id = self.request.GET['publicacion_id']
    except KeyError:
      self.redirect("/verEntradas")
      return

    usr = users.get_current_user()
    usr_info = usuario.devolver(usr)

    if usr and usr_info:
      usr_info.log = "LogOut"
      access_link = users.create_logout_url("/")

      try:
        publicacion = ndb.Key(urlsafe=id).get()
      except:
        self.redirect("publicaciones/verPublicacion?publicacion_id=" + id)
        return

      template_values = {

        "usr_info": usr_info,
        "access_link": access_link,
        "publicacion": publicacion,
        "titulo": Publicacion.titulo,
        "descripcion": Publicacion.descripcion,
        "url": Publicacion.url
      }

      jinja = jinja2.get_jinja2(app=self.app)
      self.response.write(jinja.render_template("modificarPublicacion.html", **template_values))
    else:
      self.redirect("/")

  def post(self):
    try:
      id = self.request.GET['publicacion_id']
    except KeyError:
      id = None

    if not id:
      self.redirect("/verEntradas")
      return

    user = users.get_current_user()
    usr_info = usuario.devolver(user)

    if user and usr_info:
      usr_info.log = "LogOut"
      access_link = users.create_logout_url("/")
      try:
        publicacion = ndb.Key(urlsafe=id).get()
      except KeyError:
        self.redirect("/publicaciones/verPublicacion?publicacion_id=" + id)
        return
      publicacion = Publicacion()
      publicacion.titulo = self.request.get("titulo", "").strip()
      publicacion.descripcion = self.request.get("descripcion", "").strip()
      publicacion.url = self.request.get("url", "").strip()
      key = publicaciones.update(publicacion)

      self.redirect("/publicaciones/verPublicacion?publicacion_id=" + key.urlsafe())
    else:
      self.redirect("/")


app = webapp2.WSGIApplication([
  ("/publicaciones/modificarPublicacion", ModificarPublicacion),
], debug=True)
