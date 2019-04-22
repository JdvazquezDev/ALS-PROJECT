import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
from model.usuario import Usuario


class BienvenidoHandler(webapp2.RequestHandler):

  def get(self):
    user = users.get_current_user()
    usr_info = Usuario.retrieve(user)

    if user and usr_info:
      self.redirect("/verEntradas")
      return
    else:
      usr_info = Usuario.create_empty_user()
      usr_info.nick = "Login"
      access_link = users.create_login_url("/verEntradas")

    template_values = {
      "usr_info": usr_info,
      "access_link": access_link
    }

    jinja = jinja2.get_jinja2(app=self.app)
    self.response.write(jinja.render_template("template.html", **template_values))


app = webapp2.WSGIApplication([
  ('/', BienvenidoHandler),
], debug=True)
