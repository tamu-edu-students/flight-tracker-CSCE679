from flask import Flask, jsonify, request, session
import live

# live.get_languages()
app = Flask(__name__)

@app.route('/', methods=['GET']) #, methods=['POST'])
def homepage():
    return "Home Page!!"

@app.route('/login') #, methods=['POST'])
def login():
    return "Hello"

@app.route('/language') #, methods=['POST'])
def language():
    return jsonify(live.get_languages())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)