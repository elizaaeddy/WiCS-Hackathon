from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from .models import Assignment, Student
from django.utils import timezone

from assignments.models import Student


class IndexView(generic.ListView):
    template_name = 'assignments/index.html'
    model = Assignment
    context_object_name = 'assignment_list'
    paginate_by = 5


# Create your views here.

class todoView(ListView):
    model = Assignment
    assignment_list = Assignment.objects.all()
    template_name = 'assignments/todo.html'

