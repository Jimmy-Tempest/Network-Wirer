from django.contrib import admin
from .models import *


class DatasetAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'description', 'owner')
    filter_horizontal = ("libraryOf", )


class ModelAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'description', 'owner')


# Register your models here.
admin.site.register(User)
admin.site.register(Dataset, DatasetAdmin)
admin.site.register(NeuralNetworkModel, ModelAdmin)
