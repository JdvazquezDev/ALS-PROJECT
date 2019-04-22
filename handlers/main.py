#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import users
import jinja2
from model.usuario import Usuario


class MainHandler(webapp2.RequestHandler):
  UsuarioAnonimo = "anónimo"

  def post(self):
    usr = users.users.get_current_user()

    if usr:
      login_url = users.users.create_logout_url()
    else:
      login_url = users.users.create_login_url()

      # obtener datos del formulario

      nombre = self.request.get("edNombre", MainHandler.UsuarioAnonimo)
      if len(nombre.strip()) == 0:
        nombre = MainHandler.UsuarioAnonimo

        # Crear la plantilla para devolver los datos
        datos = {
          "usr_name": nombre,
          "usuarios": usr.query(),
          "login_logout_url": login_logout_url,
          "usr": usr
        }

  # Crear nuevo usuario
  if usr:
    email = usr.email()
  else:
    email = "anonymous@anonymous.com"


app = webapp2.WSGIApplication([
  ('/', MainHandler)
], debug=True)
