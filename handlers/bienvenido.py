
import webapp2

from webapp2_extras import jinja2

from google.appengine.api import users
import model.usuario as usuario

class BienvenidoHandler(webapp2.RequestHandler):

  def get(self):
    Usuario = users.get_current_user()
    usr_info = usuario.devolver(Usuario)

    if Usuario and usr_info:
      self.redirect("/verEntradas")
      return
    else:
      usr_info = usuario.create_empty_user()
      usr_info.log = "Login"
      access_link = users.create_login_url("/verEntradas")

    template_values = {
      "usr_info": usr_info,
      "access_link": access_link
    }

    jinja = jinja2.get_jinja2(app=self.app)
    self.response.write(jinja.render_template("index.html", **template_values))


app = webapp2.WSGIApplication([
  ('/', BienvenidoHandler),
], debug=True)
