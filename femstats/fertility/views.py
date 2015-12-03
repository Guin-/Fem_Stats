from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from femstats.fertility.models import Period
from femstats.fertility.forms import PeriodForm

class PeriodsList(LoginRequiredMixin, ListView):
    model = Period
    template_name = "fertility/period_list.html"
    context_object_name = 'period_list'

    def get_queryset(self):
        '''
        Filter data to display entries from the currently logged in user
        '''
        return Period.objects.filter(user = self.request.user)

# Form submits, a model instance is saved.
# However it redirects to fertility/periods/add/fertility/periods
class PeriodCreate(LoginRequiredMixin, CreateView):
    model = Period
    template_name = "fertility/period_form.html"
    form_class = PeriodForm
    success_url = "fertility/periods/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PeriodCreate, self).form_valid(form)

# absolute_url on period model now works as success_url
class PeriodUpdate(LoginRequiredMixin, UpdateView):
    model = Period
    template_name = "fertility/period_form.html"
    form_class = PeriodForm

class PeriodDetail(LoginRequiredMixin, DetailView):
    model = Period
    template_name = "fertility/period_detail.html"
    context_object_name = "period"

class PeriodDelete(LoginRequiredMixin, DeleteView):
    model = Period

