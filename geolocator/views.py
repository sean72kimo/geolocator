from django.shortcuts import render_to_response, RequestContext
from thirdParty.functions import locu_search, foursquare_search
from locations.models import Location


def home(request):
	if request.method == 'POST':
		print(type(request.POST))
		print('request.POST= {0}'.format(request.POST))

		query = request.POST['search']
		print('query= {0}'.format(query))
		locations = locu_search(query)
		for loc in locations:
			name, locuOrFour_id = loc[0], loc[1]
			new_location, created = Location.objects.get_or_create(name = name, 
																   locuOrFour_id = locuOrFour_id,
																   src_site = 'locu',
																   city = query)
			if created:
				print('Created new id {0} for {1}'.format(locuOrFour_id, name))
		# locations=foursquare_search(query)
		print('locations= {0}'.format(locations))

	return render_to_response('home.html', locals(), context_instance=RequestContext(request))

