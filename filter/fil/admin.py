from django.contrib import admin
from.models import *
from .filter import *
from django.contrib.admin.filters import AllValuesFieldListFilter

class PersonAdmin(admin.ModelAdmin):
    # display the list in the front
    list_display = ('name','price2')
    # shows filter tag at the right side of the table
    list_filter =(ProjectFilter,('price2',PriceFilter),)
    # searching on the basis of fields name inside the Project Table
    search_fields = ['name','price2']

admin.site.register(Project,PersonAdmin)
admin.site.register(BD)
