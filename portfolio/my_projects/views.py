from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from my_projects.models import Project
from my_projects.forms import ProjectForm


from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ProjectListView(ListView):
    model = Project

    def get_queryset(self):
        return Project.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class ProjectDetailView(DetailView):
    model = Project


class CreateProjectView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'my_projects/project_draft_list.html'

    form_class = ProjectForm

    model = Project


class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'my_projects/post_draft_list.html'

    form_class = ProjectForm

    model = Project


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'my_projects/project_draft_list.html'

    model = Project

    def get_queryset(self):
        return Project.objects.filter(published_date__isnull=True).order_by('created_date')


class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Project
    success_url = reverse_lazy('my_projects:project_draft_list')

#######################################
## Functions that require a pk match ##
#######################################

@login_required
def project_publish(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.publish()
    return redirect('my_projects:project_detail', pk=pk)

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'my_projects/model_form_upload.html', {
        'form': form
    })