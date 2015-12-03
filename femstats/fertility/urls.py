from django.conf.urls import url
from femstats.fertility import views

urlpatterns = [
    # URL pattern for the PeriodListView
    url(
        regex=r'periods/$',
        view=views.PeriodsList.as_view(),
        name='periods'
    ),
    url(
        regex=r'^periods/add/$',
        view=views.PeriodCreate.as_view(),
        name='period_create'
    ),
    url(
        regex=r'^periods/update/(?P<pk>\d+)$',
        view=views.PeriodUpdate.as_view(),
        name='period_update'
    ),
    url(
        regex=r'^period/(?P<pk>\d+)$',
        view=views.PeriodDetail.as_view(),
        name='period'
    ),
]
