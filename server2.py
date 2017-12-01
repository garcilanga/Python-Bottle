from bottle import route, run, template

@route('/')
@route('/hello/<name>')
def hello(name='Stranger'):
    return template('<h1>Hello {{name}}, how are you?</h1>!', name=name)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)

    
