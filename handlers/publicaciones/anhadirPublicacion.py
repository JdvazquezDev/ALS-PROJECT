import webapp2
from google.appengine.api import users


import model.publicacion as publicacion
import model.usuario as usuario


class AnhadirPublicacion(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        usr_info = usuario.devolver(user)

        if user and usr_info:

            usr_info.log = "LogOut"
            access_link = users.create_logout_url("/")
            key = publicacion.update(publicacion.create())
            self.redirect("/publicaciones/modificarPublicacion?publicacion_id=" + key.urlsafe())
        else:
            self.redirect("/")

        return


app = webapp2.WSGIApplication([
    ("/publicaciones/anhadirPublicacion", AnhadirPublicacion),
], debug=True)
