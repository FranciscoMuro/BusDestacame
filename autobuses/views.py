#Utils
from re import template
from django.shortcuts import render
#Views
from django.views.generic.edit import CreateView, UpdateView
#Forms
from .forms import AutobusForm
#Models
from autobuses.models import Autobus

class CreateBus(CreateView):
    template_name = createBusTemplate.html
    model = Autobus
    form_class = AutobusForm
