# requires bottle.py 
# pip install bottle
# or download directly from http://bottlepy.org/bottle.py

from bottle import route, run, template
from bottle import get, post, request

@route('/hello')
def hello():
  return "Hello World"

@route('/')
def menu():
  # expects "menu.html" in views directory
  return template("menu.html")

@route('/hello/<name>')
def greet(name='Stranger'):
  return template('Hello {{ name }}, how are you doing?', name = name)

@get('/login')
def login():
  # expects form.html with userName and password fields
  # in 'views' subdirectory
  return template("form.html")

@post('/login')
def do_login():
  userName = request.forms.get('userName')
  password = request.forms.get('password')
  if password == "bottle":
    return "<h2>valid login, " + userName + ".</h2>"
  else:
    return "<h2>invalid login!</h2>"

run(host= "localhost", port = 8080, debug = True)


