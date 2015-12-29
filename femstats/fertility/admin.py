from django.contrib import admin
from femstats.fertility.models import Period, Fertility

class PeriodAdmin(admin.ModelAdmin):
    list_display = ('user','date','flow')

admin.site.register(Period, PeriodAdmin)

class FertilityAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'temperature',
                    'position', 'mucus', 'texture', 'opening')

admin.site.register(Fertility, FertilityAdmin)
