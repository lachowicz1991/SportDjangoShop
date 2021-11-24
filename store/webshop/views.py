from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, DeleteView, UpdateView, ListView, DetailView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import GearFilter
from django.urls import reverse_lazy
from .forms import GearForm, OutfitForm
from logging import getLogger
LOGGER = getLogger()
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class EmployeeView(TemplateView):
    template_name = 'employee.html'

class OutfitListView(ListView):
    template_name = 'outfit.html'
    model = Outfit
    context_object_name = 'outfit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = GearFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return GearFilter(self.request.GET, queryset=queryset).qs

class GearListView(ListView):
    template_name = 'gear.html'
    model = Gear
    context_object_name = 'gear'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = GearFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return GearFilter(self.request.GET, queryset=queryset).qs

class GearDetailView(DetailView):
    model = Gear
    template_name = 'gear_detail.html'
    context_object_name = 'gear_detail'


class OutfitDetailView(DetailView):
    model = Outfit
    template_name = 'outfit_detail.html'
    context_object_name = 'outfit_detail'

class GearCreateView(LoginRequiredMixin, CreateView):
    template_name = 'gear_form.html'
    form_class = GearForm
    success_url = reverse_lazy('gear')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        # Gear.objects.create(
        #     gear_name=cleaned_data['gear_name'])
        return result

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data!')
        return super().form_invalid(form)

class OutfitCreateView(LoginRequiredMixin, CreateView):
    template_name = 'outfit_form.html'
    form_class = OutfitForm
    success_url = reverse_lazy('outfit')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        # Outfit.objects.create(
        #     gear_name=cleaned_data['outfit_name'])
        return result

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data!')
        return super().form_invalid(form)


class GearUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'gear_form.html'
    model = Gear
    form_class = GearForm
    success_url = reverse_lazy('gear')

class OutfitUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'outfit_form.html'
    model = Outfit
    form_class = OutfitForm
    success_url = reverse_lazy('outfit')

class OutfitDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'outfit_delete.html'
    model = Outfit
    success_url = reverse_lazy('outfit')

class GearDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'gear_delete.html'
    model = Gear
    success_url = reverse_lazy('gear')

def outfit_sort(request):
    sorting = request.GET.get('s', 'default')

    if sorting == 'outfit_name':
        outfit_list = Outfit.objects.all().order_by('gear_name')
    elif sorting == 'price':
        outfit_list = Outfit.objects.all().order_by('price')
    # elif sorting == 'sport_branch':
    #     gear_list = Gear.objects.all().order_by('sport_branch')

    else:
        outfit_list = Outfit.objects.all()

    return render(request, template_name='outfit.html', context={'outfit': outfit_list})

def gear_sort(request):
    sorting = request.GET.get('s', 'default')

    if sorting == 'gear_name':
        gear_list = Gear.objects.all().order_by('gear_name')
    elif sorting == 'price':
        gear_list = Gear.objects.all().order_by('price')
    # elif sorting == 'sport_branch':
    #     gear_list = Gear.objects.all().order_by('sport_branch')

    else:
        gear_list = Gear.objects.all()

    return render(request, template_name='gear.html', context={'gear': gear_list})
