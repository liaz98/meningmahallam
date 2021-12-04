from django.urls import path
from . import views

urlpatterns =[

    path('about/', views.NeighborhoodView.as_view()),
    path('about/<str:pk>', views.NeighborhoodDetailView.as_view()),
    path('properties/', views.PropertyList.as_view()),
    path('properties/<str:pk>', views.PropertyDetailView.as_view()),
    path('vacancies/', views.VacancyListView.as_view()),
    path('vacancies/<str:pk>', views.VacancyDetailView.as_view()),
    path('streets/', views.VacancyDetailView.as_view()),
    path('streets/<str:pk>', views.VacancyDetailView.as_view()),

]