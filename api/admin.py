from django.contrib import admin

# Register your models here.
from api.models import Neighborhood, Property, Vacancy, Street

admin.site.register(Neighborhood)
admin.site.register(Property)
admin.site.register(Vacancy)
admin.site.register(Street)
