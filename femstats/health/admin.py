from django.contrib import admin
from femstats.health.models import Health

class HealthAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'sleep', 'alcohol_intake', 'exercise', 'stress_level')

admin.site.register(Health, HealthAdmin)
