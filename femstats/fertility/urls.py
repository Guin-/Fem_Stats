from django.conf.urls import url
from femstats.fertility import views

urlpatterns = [
    # URL pattern for the PeriodListView
    url(
        regex=r'^periods/$',
        view=views.PeriodsList.as_view(),
        name='period_list'
    ),
    url(
        regex=r'^periods/add/$',
        view=views.PeriodCreate.as_view(),
        name='period_create'
    ),
]
