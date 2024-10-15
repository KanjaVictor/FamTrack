from django.urls import path
from . import views

#Define a list of URL patterns
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('fam/', views.FamilyListView.as_view(), name='family-list'),
    
    path('fam/<int:pk>', views.FamilyMemberDetailView.as_view(), name='family-detail'),
]