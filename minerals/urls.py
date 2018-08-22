from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'random/', views.random_mineral, name='random'),
    url(r'search/', views.search, name='name_search'),
    url(r'(?P<pk>\d+)/', views.mineral_detail, name='detail'),
    url(r'group_(?P<group>\w+)/', views.search_group, name='group_search'),
    url(r'letter_(?P<letter>[a-z])/', views.search_letter,
        name='letter_search'),
]
