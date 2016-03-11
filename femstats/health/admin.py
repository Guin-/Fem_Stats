from django.contrib import admin
from femstats.health.models import Physical, Mental

class PhysicalAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'sleep')

admin.site.register(Physical, PhysicalAdmin)

class MentalAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')

admin.site.register(Mental, MentalAdmin)

