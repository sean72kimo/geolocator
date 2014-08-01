from geopy import geocoders
g = geocoders.GoogleV3()

def find():
	query = input('Input a place for search: ')
	place, (lat, lng) = g.geocode(query)
	return place, lat, lng

print(find())