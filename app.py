#impot flask
from flask import Flask


app = Flask(__name__)

#buat routing
@app.route('/')
def index():
    return "hello world!"

@app.route('/alvian')
def alvian():
    return "hello Alvian!"

if __name__=='__main__':
    app.run(debug=True)
