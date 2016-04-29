from dbhelper import DBHelper
from flask import Flask
from flask import render_template
from flask import request
import json
import string

app = Flask(__name__)
DB = DBHelper()
categories = ['American', 'Chinese', 'Italian', 'Pizza', 'Irish Pub', 'Brazilian', 'Mexican', 'Ethipoian']

@app.route('/')
def home():
	restaurants = DB.get_all_restaurants()
	restuarants = json.dumps(restaurants)
	return render_template('home.html', restaurants=restaurants, categories=categories)

@app.route('/add', methods=['POST'])

@app.route('/clear')

@app.route('/submit_rest', methods=['POST'])
def submit_rest():
	category = request.form.get('category')
	if category not in categories:
		return home()
	try:
		latitude = float(request.form.get('latitude'))
		longitude = float(request.form.get('longitude'))
	except ValueError:
		return home()	
	description = sanitize_string(request.form.get('description'))
	DB.add_rest(category, latitude, longitude, description)
	return home()

def sanitize_string(userinput):
	whitelist = string.letters + string.digits + " !?$.,;:-'()&"
	return filter(lambda x: x in whitelist, userinput)

if __name__ == '__main__':
	app.run(port=5000, debug=True)
