import urllib.request
import json
from io import StringIO


api_key = 'f2043f05bda1feeefdbb262a37b07b0ec2c08d33'
url = 'https://api.locu.com/v1_0/venue/search/?'
local = 'Newport Beach'
locality = local.replace(' ', '%20')

# https://api.locu.com/v1_0/venue/search/?locality=newport%20beach&api_key=f2043f05bda1feeefdbb262a37b07b0ec2c08d33
new_url = url + 'locality=' + locality + '&api_key=' + api_key

print(new_url)

obj =urllib.request.urlopen(new_url)
data = obj.read()

fileObj = StringIO(data.decode('utf-8'))
json_data = json.load(fileObj)

# for abc in json_data['objects']:
#     print(abc['name'])


menu_url = 'https://api.locu.com/v1_0/menu_item/search/?locality=Newport%20Beach&api_key=f2043f05bda1feeefdbb262a37b07b0ec2c08d33'

obj =urllib.request.urlopen(menu_url)
data = obj.read()

fileObj = StringIO(data.decode('utf-8'))
json_data = json.load(fileObj)

for abc in json_data['objects']:
	try:
		print(abc['name'] + ' at '+ abc['venue']['name'])
	except Exception:
		pass


