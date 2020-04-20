from flask import Flask, escape, request, render_template
from forsearch import searchreq
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search', methods=['POST'])
def search():
    """if POST, query movie api for data and return results."""
    title=request.form['title']
    jsonresp=searchreq(title)
    results=jsonresp["Search"]
    return render_template("search_results.html",results=results)

@app.errorhandler(404)
def notfound(error):
    return render_template('notfound.html'),404



if __name__=="__main__":
    app.run(debug=True)
