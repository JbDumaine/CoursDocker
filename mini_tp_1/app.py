import sys, os
from flask import Flask
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
@app.route('/hello/<user>')
def hello_world(user=None):
    user = user or 'BG'
    return '''
    <html>
        <head>
            <title>Templating in Flask</title>
        </head>
        <body>
            <h1>Hello %s!</h1>
            <p>Welcome to the world of JB !</p>
        </body>
    </html>''' % user
       
if __name__ == '__main__':
    app.run()
