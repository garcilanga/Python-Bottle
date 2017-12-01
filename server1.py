from bottle import route, run

@route('/')
@route('/hello/<name>')
def hello(name='Stranger'):
    return '<b>Hello %s</b>!' % name

run(host='localhost', port=8080, debug=True)

