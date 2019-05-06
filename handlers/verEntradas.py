import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb


from model.publicacion import Publicacion
import model.publicacion as publicacion
import model.usuario as usuario


class verEntradasHandler(webapp2.RedirectHandler):
  def get(self):

    Usuario = users.get_current_user()
    usr_info = usuario.devolver(Usuario)
    if Usuario and usr_info:
      usr_info.log = "LogOut"
      access_link = users.create_logout_url("/")

      try:
        publicaciones = Publicacion.query()
      except:
         self.redirect("/error")
         return


    template_values = {
      "titulo": Publicacion.titulo,
      "descripcion": Publicacion.descripcion,
      "url": Publicacion.url,
      "usr_info": usr_info,
      "access_link": access_link
    }
    jinja = jinja2.get_jinja2(app=self.app)
    publi = [x for x in publicaciones]
    template_values["publicaciones"] = publi
    self.response.write(jinja.render_template("verEntradas.html", **template_values))

app = webapp2.WSGIApplication([
  ('/verEntradas', verEntradasHandler),
  ], debug=True)
