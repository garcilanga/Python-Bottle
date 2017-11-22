from bottle import route, run

@route('/')
app = application = bottle.default_app()@route('/hello/<name>')
def greet(name='Stranger'):
    return '<h1>Hello %s, how are you?</h1>' % name

if __name__ == '__main__':
    run(host='localhost', port=8888, debug=True)
