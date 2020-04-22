from flask import Flask, escape, request, render_template,session,flash
from forsearch import searchreq
import json
import requests
from datetime import timedelta
app = Flask(__name__)
app.config["SESSION_PERMANENT"]=True

#This is how much favourite movie data last
app.config["PERMANENT_SESSION_LIFETIME"]=timedelta(days=31)

'''
##copy and run this code in python terminal
from hashlib import sha256
text=csaju.encode("utf-8")
text=sha256(text).hexdigest()
print(text)
#output is d273fd202ae36a79dd36f160616859903861e535d49b44793b1d2930b05ff33a
'''

#and encoded in hexadecimal
#for session
app.secret_key="d273fd202ae36a79dd36f160616859903861e535d49b44793b1d2930b05ff33a"

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
	try:
		jsonresp=searchreq(title)
		results=jsonresp["Search"]
		return render_template("search_results.html",results=results)
	except Exception as e:
		return render_template("notfound.html"),404

@app.route('/favourites',methods=['POST','GET'])
def favourite():
	if request.method=="GET":
		results=session.get("fav")
		print(results)
		flash("Favourite movies last only for 31 days")
		if results!=None:
			return render_template('favourites.html',results=results)
		else:
			return '<h1>Sorry</h1>'

	elif request.method=="POST":
		poster=request.form["poster"]
		Title=request.form["title"]
		Year=request.form["year"]
		imdbID=request.form["imdb"]
		Type=request.form["type"]
		#templating the movie as in result
		currentmovie={
			"Type":Type,
			"Poster":poster,
			"Title":Title,
			"Year":Year,
			"imdbID":imdbID
		}
		print(session)
		try:
			listoffav=session["fav"]
			listoffav.append(currentmovie)

		except:
			listoffav=[]
			listoffav.append(currentmovie)

		session["fav"]=listoffav
		
		return (redirect(url_for("favourite")))


@app.errorhandler(404)
def notfound(error):
	return render_template('notfound.html'),404



if __name__=="__main__":
	app.run(debug=True)
