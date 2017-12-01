from bottle import route, run, template

@route('/')
@route('/hello/<name>')
def hello(name='Stranger'):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080, debug=True)
