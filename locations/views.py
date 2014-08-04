from django.shortcuts import render
from django.shortcuts import render_to_response, RequestContext
from .models import Location


def single_location(request, id):
	try:
		location = Location.objects.get(locuOrFour_id = id)
	except Location.DoesNotExist:
		location = Location.objects.get(locuOrFour_id = id)
	except:
		location = 'This Location Cannot Be Found'
	return render_to_response('locations/single.html', locals(), context_instance = RequestContext(request))


