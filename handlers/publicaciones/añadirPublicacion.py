import webapp2
from google.appengine.api import users


import model.publicacion as publicaciones
import model.usuario as usuario


class AñadirPublicacion(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        usr_info = usuario.devolver(user)

        if user and usr_info:
            key = publicaciones.update(publicaciones.create(usr_info))
            self.redirect("/publicaciones/modificarPublicacion?publicacion_id=" + key.urlsafe())
        else:
            self.redirect("/")

        return


app = webapp2.WSGIApplication([
    ("/publicaciones/añadirPublicacion", AñadirPublicacion),
], debug=True)
