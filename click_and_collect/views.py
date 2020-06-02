from django.shortcuts import render
from .models import ClickCollectLocations


def click_and_collect(request):
	"""
	Renders the click&collect dropoff locations
	and makes use of the Google Maps API
	"""

	locations = ClickCollectLocations.objects.all()

	return render(request, 'click_and_collect/click_and_collect_locations.html',
		{'locations': locations})
