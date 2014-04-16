from flask import Flask, render_template, url_for, redirect
from extract import get_json_data

app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('gain_nifty'))

@app.route('/gainers/nifty')
def gain_nifty():
    data = get_json_data('gain',0)
    return render_template("home.html", title = "Top Gainers Nifty", data = data)

@app.route('/gainers/jrnifty')
def gain_jrnifty():
    data = get_json_data('gain',1)
    return render_template("home.html", title = "Top Gainers Jr. Nifty", data = data)

@app.route('/losers/nifty')
def loss_nifty():
	data = get_json_data('loss',0)
	return render_template("home.html", title = "Top Losers Nifty", data = data)

@app.route('/losers/jrnifty')
def loss_jrnifty():
	data = get_json_data('loss',1)
	return render_template("home.html", title = "Top Gainers Jr. Nifty", data = data)