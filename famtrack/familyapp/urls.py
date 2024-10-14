from django.urls import path
from . import views

#Define a list of URL patterns
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('family/', views.FamilyMemberListView.as_view(), name='familymembers')
]