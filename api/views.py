from django.shortcuts import render
from .models import Neighborhood, Property, Vacancy, Street
from .serializers import NeighborhoodSerializer, PropertySerializer, VacancySerializer, StreetSerializer
from rest_framework import generics
import json

class NeighborhoodView(generics.ListCreateAPIView):
    queryset = Neighborhood.objects.all()
    # # f = open("624-1527_1651_1829.json")
    # f = open("C:/Users/User/Documents/Projects/learners/meningmahallam/api/624-1527_1651_1829.json")
    #
    # # returns JSON object as
    # # a dictionary
    # data = json.load(f)
    #
    # # Iterating through the json
    # # list
    # for i in range(len(data)):
    #     Neighborhood.objects.create(
    #         district=data[i]['G2'],
    #         address=data[i]['G4'],
    #         length=data[i]['G6'],
    #         square=data[i]['G7'])
    # print(data[0])
    # # Closing file
    # f.close()
    serializer_class = NeighborhoodSerializer


class NeighborhoodDetailView(generics.RetrieveUpdateAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer


class PropertyList(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class VacancyListView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class StreetListView(generics.ListCreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class StreetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer