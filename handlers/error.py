
import webapp2
from webapp2_extras import jinja2
import model.usuario as usuario
from google.appengine.api import users
from webapp2_extras import jinja2

class ErrorHandler(webapp2.RequestHandler):
  def get(self):
    Usuario = users.get_current_user()
    usr_info = usuario.devolver(Usuario)
    if Usuario and usr_info:
      usr_info.log = "LogOut"
      access_link = users.create_logout_url("/")
    template_values = {
     "usr_info": usr_info,
     "access_link": access_link
    }

    jinja = jinja2.get_jinja2(app=self.app)
    self.response.write(jinja.render_template("error.html", **template_values));


app = webapp2.WSGIApplication([
    ("/error", ErrorHandler),
], debug=True)
