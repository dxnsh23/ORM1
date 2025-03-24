from django.contrib import admin #type: ignore
from.models import Movie,MovieAdmin
admin.site.register(Movie,MovieAdmin)

