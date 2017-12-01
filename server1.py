from bottle import route, run

@route('/')
@route('/hello/<name>')
def hello(name='Stranger'):
    return '<h1>Hello %s, how are you?</h1>' % name

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)

