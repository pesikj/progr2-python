from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.base import TemplateView
from . import models
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = "index.html"

class ContactsView(TemplateView):
    template_name = "contacts.html"
  
class AboutView(TemplateView):
    template_name = "about.html"

class CourseListView(ListView):
    model = models.Course
    template_name = "course_list.html"

class BranchListView(ListView):
    model = models.Branch
    template_name = "branch_list.html"

class PersonListView(ListView):
    model = models.Person
    template_name = "person_list.html"

# Verze z první poloviny

# class ApplicationCreateView(CreateView):
#     model = models.Application
#     template_name = "application_create.html"
#     fields = ["email", "first_name", "last_name", "motivation", "course"]
#     success_url = reverse_lazy("application_confirmation")

class ApplicationCreateView(CreateView):
    model = models.Application
    template_name = "application_create.html"
    fields = ["email", "first_name", "last_name", "motivation", "course"]
    success_url = reverse_lazy("application_confirmation")

    def form_valid(self, form):
        course_id = self.kwargs['pk']
        course = models.Course.objects.get(pk=course_id)
        form.instance.course = course
        return super().form_valid(form)

class ApplicationConfirmation(TemplateView):
    template_name = "application_confirmation.html"

class PersonRegisterView(CreateView):
    model = models.Person
    fields = ["first_name", "last_name", "email"]
    template_name = "person_register.html"
    success_url = reverse_lazy("application_confirmation")

class CourseDetailView(DetailView):
    model = models.Course
    template_name = "course_detail.html"

class BranchDetailView(DetailView):
    model = models.Branch
    template_name = "branch_detail.html"

