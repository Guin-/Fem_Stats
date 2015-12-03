from django.contrib import admin
from femstats.fertility.models import Period

class PeriodAdmin(admin.ModelAdmin):
    pass

admin.site.register(Period, PeriodAdmin)
