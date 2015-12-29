from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from femstats.fertility.models import Period, Fertility
from femstats.fertility.forms import PeriodForm, FertilityForm

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
    success_url = reverse_lazy('fertility:periods')

class FertilityCreate(LoginRequiredMixin, CreateView):
    form_class = FertilityForm
    template_name = "fertility/fertility_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FertilityCreate, self).form_valid(form)

class FertilityUpdate(LoginRequiredMixin, UpdateView):
    form_class = FertilityForm
    template_name = "fertility/fertility_form.html"

class FertilityDetail(LoginRequiredMixin, DetailView):
    model = Fertility
    template_name = "fertility/fertility_detail.html"
    context_object_name = "fertility"

class FertilityDelete(LoginRequiredMixin, DeleteView):
    model = Fertility
    success_url = reverse_lazy('fertility:fertility_list')

class FertilityList(LoginRequiredMixin, ListView):
    model = Fertility
    template_name = "fertility/fertility_list.html"
    context_object_name = 'fertility_list'

    def get_queryset(self):
        '''
        Filter data to display entries from the currently logged in user
        '''
        return Fertility.objects.filter(user = self.request.user)


