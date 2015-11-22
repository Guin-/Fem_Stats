from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin

from femstats.fertility.models import Period as PeriodModel
from femstats.fertility.forms import PeriodForm

class PeriodsList(LoginRequiredMixin, ListView):
    model = PeriodModel
    template_name = "fertility/period_list.html"
    context_object_name = 'Periods'

class PeriodCreate(LoginRequiredMixin, CreateView):
    model = PeriodModel
    template_name = "fertility/period_form.html"
    form_class = PeriodForm
#    success_url =

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PeriodCreate, self).form_valid(form)

class PeriodUpdate(LoginRequiredMixin, UpdateView):
    pass

class PeriodDelete(LoginRequiredMixin, DeleteView):
    pass


