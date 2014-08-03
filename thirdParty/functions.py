import urllib.request
import json
from io import StringIO




def locu_search(query):
	api_key = 'f2043f05bda1feeefdbb262a37b07b0ec2c08d33'
	url = 'https://api.locu.com/v1_0/venue/search/?'
	local = query
	locality = local.replace(' ', '%20')
	# https://api.locu.com/v1_0/venue/search/?locality=newport%20beach&api_key=f2043f05bda1feeefdbb262a37b07b0ec2c08d33
	full_url = url + 'locality=' + locality + '&api_key=' + api_key

	obj =urllib.request.urlopen(full_url)
	data = obj.read()
	fileObj = StringIO(data.decode('utf-8'))
	json_data = json.load(fileObj)
	locations = []
	for abc in json_data['objects']:
		locations.append(abc['name'])
	return locations




def foursquare_search(query):
	token = '2NZH5OFJXGFSCDHY5MB2HQAI40JXOWAML1PS32LAW4GCJTVJ'
	lat = '33.6167'
	lng = '-117.8975'
	latlng = lat + '%2C' + lng
	ll=33.6167-117.8975

	url = 'https://api.foursquare.com/v2/venues/search?v=20131016&'+ latlng +'&intent=checkin&oauth_token='
	full_url = url + token
	obj =urllib.request.urlopen(full_url)
	data = obj.read()
	print(type(data.decode('utf-8')))
	fileObj = StringIO(data.decode('utf-8'))
	json_data = json.load(fileObj)

	# print(j_data['response'])
	for abc in json_data['response']['venues']:
		print(abc['name'])
		try:
			print('phone =', abc['contact']['phone'])
		except Exception:
			pass
		try:
			print('twitter =', abc['contact']['twitter'])
		except Exception:
			pass
		try:
			print('city =', abc['location']['city'])
		except Exception:
			pass
