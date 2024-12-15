from flask import Flask


app = Flask(__name__)

#@app.route('/')
#def index():
#    return 'Hello, World!'

@app.route('/one')
def one():
    return 'one', 201

@app.route('/two')
def two():
    return 'two', 202

@app.route('/three')
def three():
    return 'three', 203

@app.route('/four')
def four():
    return 'four', 204

@app.route('/five')
def five():
    return 'five', 205

@app.route('/error')
def error():
    return 'error', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')