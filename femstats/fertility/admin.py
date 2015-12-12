from django.contrib import admin
from femstats.fertility.models import Period

class PeriodAdmin(admin.ModelAdmin):
    list_display = ('user','date','flow')

admin.site.register(Period, PeriodAdmin)
