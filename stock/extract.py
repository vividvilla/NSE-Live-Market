import requests
from bs4 import BeautifulSoup, Comment

def find_data(var):
	"""
	Finds all 'onclick' property from the soup and returns it as a dictionary.
	"""
	dict_data = []
	p = var.find_all('a')
	for link in range(2):
		data = p[link].get('onclick').split(';')
		new_data = {}
		for i in data:
			k,l = i.split('=')
			new_data[k] = l.strip("'")
		dict_data.append(new_data)

	return dict_data

def get_json(gl,ty):
	"""
	Creates a link from gl and ty and retirves the json data for the same [This proprty observed from the NSE Source]
	"""
	link = 'http://www.nseindia.com/live_market/dynaContent/live_analysis/'+ gl[:-1].lower() + '/' + ty + gl + '.json'
	r = requests.get(link)
	return r.json()

def get_json_data(trend, num):
	"""
	Accepts two variable 'trend' and 'num'. 'trend' defines the type (loss or gain)
	'num' variable defines array index. 'num' = 0 ==> Nifty data and 'num' = 1 ==> Jr.Nifty data
 
	"""
	maindata = requests.get('http://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm').text
	mainsoup = BeautifulSoup(maindata)

	comments = mainsoup.findAll(text=lambda text:isinstance(text, Comment))
	for comment in comments:
		comment.extract()

	if trend == 'gain':
		gainers = mainsoup.find(id="tab7Content")
		gainers_data = find_data(gainers)
		gl = gainers_data[num]['gl']
		ty = gainers_data[num]['ty']
		return get_json(gl,ty)
	else:
		losers = mainsoup.find(id="tab8Content")
		losers_data = find_data(losers)
		gl = losers_data[num]['gl']
		ty = losers_data[num]['ty']
		return get_json(gl,ty)
