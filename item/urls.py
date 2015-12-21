from django.conf.urls import url
from django.views import generic

from .views import AlCreateView, AlUpdateView, S2CreateView, S2UpdateView


urlpatterns = [
    url('^s2/create/$',
        S2CreateView.as_view(),
        name='s2_item_create'),
    url('^s2/update/(?P<pk>\d+)/$',
        S2UpdateView.as_view(),
        name='s2_item_update'),
    url('^al/create/$',
        AlCreateView.as_view(),
        name='al_item_create'),
    url('^al/update/(?P<pk>\d+)/$',
        AlUpdateView.as_view(),
        name='al_item_update'),
]
