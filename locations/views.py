from django.shortcuts import render
from django.shortcuts import render_to_response, RequestContext
from .models import Location
from thirdParty.functions import locu_details


def single_location(request, loc_id):
    try:
        location = Location.objects.get(locuOrFour_id = loc_id)
        locu = True
    except Location.DoesNotExist:
        location = Location.objects.get(locuOrFour_id = loc_id)
        foursquare = True
    except:
        location = 'This Location Cannot Be Found'

    if locu:
        details = locu_details(loc_id)
    elif foursquare:
        pass
    else:
        pass

    return render_to_response('locations/single.html', locals(), context_instance = RequestContext(request))
