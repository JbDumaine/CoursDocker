import sys, os
from flask import Flask, render_template, request,jsonify
import json

app = Flask(__name__)
json_books = open('./data/books.json',) 
books = json.load(json_books)
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/books')
def api_books():
    return jsonify(books)

@app.route('/api/books/<isbn>')
def api_book_id(isbn):
    for x in books:
        if x["isbn"] == isbn:
            return jsonify(x)
    return jsonify('"message":"no books found for "'+id)

@app.route('/api/books/title/<title>')
def api_book_title(title):
    for x in books:
        if x["title"] == title:
            return jsonify(x)
    return jsonify('"message":"no books found for "'+title)
    

if __name__ == '__main__':
    app.run()