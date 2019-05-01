# Usuario
from google.appengine.ext import ndb
from google.appengine.api import users


class Usuario(ndb.Model):
  nombre = ndb.StringProperty()
  email = ndb.StringProperty(required=True)


def create(usr):

  toret = Usuario()
  toret.email = usr.email()
  return toret


def create_empty_user():
  return Usuario(nombre="", email="")


@ndb.transactional
def update(user):
  return user.put()


def devolver(usr):
  toret = None

  if usr:
    usr_email = usr.email()
    found_users = Usuario.query(Usuario.email == usr_email)

    if (found_users.count() == 0):
      toret = create(usr)
      update(toret)
    else:
      toret = found_users.iter().next()
      toret.usr = usr

  return toret
