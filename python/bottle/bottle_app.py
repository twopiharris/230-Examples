from bottle import default_app, route, post, get, template

@route('/')
def menu():
    return template("menu.html")

@route('/basic')
def basicForm():
    return template("form.html")

@post('/convert')
def convert():
    return template("result.html")

@route('/twoWay')
def twoWay():
    return template("twoWay.html")

@post('/convertTwoWay')
def convertTwoWay():
    return template("twoWayResult.html")

application = default_app()

