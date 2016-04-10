from django.conf.urls import patterns, url

from .views import RecommendationLonLatAPIView


urlpatterns = patterns('',
                       url(r'^recommendation-lat-lon/',
                           RecommendationLonLatAPIView.as_view())
                       )
