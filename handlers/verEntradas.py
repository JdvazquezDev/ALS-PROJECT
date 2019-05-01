import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users


from model.publicacion import Publicacion
import model.usuario as usuario



class verEntradasHandler(webapp2.RedirectHandler):
  def get(self):
    Usuario = users.get_current_user()
    usr_info = usuario.devolver(Usuario)
    if Usuario and usr_info:
      usr_info.log = "LogOut"
      access_link = users.create_logout_url("/")

    template_values = {
      "titulo": Publicacion.titulo,
      "descripcion": Publicacion.descripcion,
      "usr_info": usr_info,
      "access_link": access_link
    }
    jinja = jinja2.get_jinja2(app=self.app)
    self.response.write(jinja.render_template("verEntradas.html", **template_values))

app = webapp2.WSGIApplication([
  ('/verEntradas', verEntradasHandler),
  ], debug=True)
