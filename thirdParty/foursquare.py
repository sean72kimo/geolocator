import urllib.request
import json
from io import StringIO

url = 'https://api.foursquare.com/v2/venues/search?v=20131016&ll=33.6167%2C-117.8975&intent=checkin&oauth_token=2NZH5OFJXGFSCDHY5MB2HQAI40JXOWAML1PS32LAW4GCJTVJ'

obj =urllib.request.urlopen(url)
data = obj.read()
print(type(data.decode('utf-8')))
fileObj = StringIO(data.decode('utf-8'))
json_data = json.load(fileObj)

# print(j_data['response'])
for abc in json_data['response']['venues']:
	# print(abc['name'])
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
