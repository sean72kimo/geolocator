from django.shortcuts import render_to_response, RequestContext
from thirdParty.functions import locu_search


def home(request):
	if request.method == 'POST':
		print('request.POST= {0}'.format(request.POST))
	query = request.POST['search']
	print('query= {0}'.format(query))
	locations = locu_search(query)
	print('locations= {0}'.format(locations))

	return render_to_response('home.html', locals(), context_instance=RequestContext(request))

