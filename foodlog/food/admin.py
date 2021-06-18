from django.contrib import admin
from .models import Food, Measure

# Register your models here.

class MeasureInline(admin.StackedInline):
    model = Measure

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand']
    inlines = [MeasureInline,]