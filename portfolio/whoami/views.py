from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Me
from .forms import MeForm


from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class MeListView(ListView):
    model = Me

class MeDetailView(DetailView):
    model = Me


class CreateMeView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'whoami/me_draft_list.html'

    form_class = MeForm

    model = Me


class MeUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'whoami/me_draft_list.html'

    form_class = MeForm

    model = Me


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'whoami/me_draft_list.html'

    model = Me



class MeDeleteView(LoginRequiredMixin,DeleteView):
    model = Me
    success_url = reverse_lazy('whoami:me_draft_list')

#######################################
## Functions that require a pk match ##
#######################################

@login_required
def me_publish(request, pk):
    me = get_object_or_404(Me, pk=pk)
    me.publish()
    return redirect('whoami:me_detail', pk=pk)

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = MeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MeForm()
    return render(request, 'whoami/model_form_upload.html', {
        'form': form
    })