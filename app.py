from flask import Flask
import sqlalchemy


app = Flask(__name__)


@app.route('/')
def index():
    return '<H1>Hello From Pet Adoption</H1>'


@app.route('/adopt')
def adopt():
    return '<h1>Adoption Page</h1>'


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='localhost')
