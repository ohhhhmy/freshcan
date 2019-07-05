from django.contrib import admin
from .models import Vegetable, Meat, Fruit, Grain, Seafood
# Register your models here.
admin.site.register(Vegetable)
admin.site.register(Meat)
admin.site.register(Fruit)
admin.site.register(Grain)
admin.site.register(Seafood)