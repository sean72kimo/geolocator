import urllib.request
import json
from io import StringIO
from geopy import geocoders





def find_place(query):
    g = geocoders.GoogleV3()
    place, (lat, lng) = g.geocode(query)
    return place, lat, lng


def locu_details(locu_id):
    url = 'https://api.locu.com/v1_0/venue/'
    locu_api_key = 'f2043f05bda1feeefdbb262a37b07b0ec2c08d33'
#   https://api.locu.com/v1_0/venue/023ec987899bed327a6d/?api_key=f2043f05bda1feeefdbb262a37b07b0ec2c08d33
    full_url = url + locu_id + '/?api_key=' + locu_api_key
#     print('locu_details=', full_url)
    obj =urllib.request.urlopen(full_url)
    data = obj.read()
    fileObj = StringIO(data.decode('utf-8'))
    json_data = json.load(fileObj)

    details = []
    for abc in json_data['objects']:
        details.append(abc['lat'])
        details.append(abc['long'])

    return details


def locu_search(query):
    locu_api_key = 'f2043f05bda1feeefdbb262a37b07b0ec2c08d33'
    url = 'https://api.locu.com/v1_0/venue/search/?'
    local = query
    locality = local.replace(' ', '%20')
    # https://api.locu.com/v1_0/venue/search/?locality=newport%20beach&api_key=f2043f05bda1feeefdbb262a37b07b0ec2c08d33
    full_url = url + 'locality=' + locality + '&api_key=' + locu_api_key

    obj =urllib.request.urlopen(full_url)
    data = obj.read()
    fileObj = StringIO(data.decode('utf-8'))
    json_data = json.load(fileObj)
    locations = []
    for abc in json_data['objects']:
        item_list = [abc['name'], abc['id']]
        locations.append(item_list)
    return locations


def foursquare_search(query):
    locations = []
    oauth_token = '2NZH5OFJXGFSCDHY5MB2HQAI40JXOWAML1PS32LAW4GCJTVJ'
    place, lat, lng = find_place(query)
    print(place, lat, lng)
    latlng = 'll=' + str(lat) + '%2C' + str(lng)

    url = 'https://api.foursquare.com/v2/venues/search?v=20131016&'+ latlng +'&intent=checkin&oauth_token='
    full_url = url + oauth_token
    print(full_url)
    obj =urllib.request.urlopen(full_url)
    data = obj.read()
    print(type(data.decode('utf-8')))
    fileObj = StringIO(data.decode('utf-8'))
    json_data = json.load(fileObj)

    # print(j_data['response'])
    for abc in json_data['response']['venues']:
        print(abc['name'])
        locations.append(abc['name'])
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
    return locations







