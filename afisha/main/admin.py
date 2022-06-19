from django.contrib import admin
from.models import *
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', )
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', )
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text',)





admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Director, DirectorAdmin)
