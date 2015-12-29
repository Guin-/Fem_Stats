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
    url(
        regex=r'^period/(?P<pk>\d+)/delete/$',
        view=views.PeriodDelete.as_view(),
        name='period_delete'
    ),
    url(
        regex=r'^add/$',
        view=views.FertilityCreate.as_view(),
        name='fertility_create'
    ),
    url(
        regex=r'^update/(?P<pk>\d+)$',
        view=views.FertilityUpdate.as_view(),
        name='fertility_update'
    ),
    url(
        regex=r'^(?P<pk>\d+)$',
        view=views.FertilityDetail.as_view(),
        name='fertility'
    ),
    url(
        regex=r'^(?P<pk>\d+)/delete/$',
        view=views.FertilityDelete.as_view(),
        name='fertility_delete'
    ),
    url(
        regex=r'history/$',
        view=views.FertilityList.as_view(),
        name='fertility_list'
    ),
]

