from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import requests

from .models import Recommendation


class RecommendationLonLatAPIView(APIView):
    def get(self, request, *args, **kw):
        lat = request.GET.get("lat")
        lon = request.GET.get("lon")
        vegetable = request.GET.get("vegetable")

        if lat and lon and vegetable:
            api_key = settings.API_KEY_OPENWEATHER

            params = {'lat': lat, 'lon': lon, 'appid': api_key}
            r = requests.get('http://api.openweathermap.org/data/2.5/weather',
                             params=params)
            temp = r.json()["main"]["temp"]
            wind_speed = r.json()["wind"]["speed"]
            recommendation = Recommendation.objects.get(vegetable__short_name=vegetable,
                                                        min_temp__lte=temp,
                                                        max_temp__gt=temp)
            content = {'recommendation': recommendation.message,
                       'wind_speed': wind_speed}
            return Response(content)
        else:
            return Response(status=400,
                            data="""Bad request parameters: lat, lon and
                                    vegetable params required""")
