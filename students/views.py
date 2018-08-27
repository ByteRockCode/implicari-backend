from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from classrooms.models import Classroom
from classrooms.views import ClassroomMixin


User = get_user_model()


class StudentMixin(ClassroomMixin):

    @cached_property
    def classroom(self):
        pk = self.kwargs.get('classroom_pk')
        return get_object_or_404(Classroom, pk=pk, creator=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(StudentMixin, self).get_context_data(*args, **kwargs)

        context['classroom'] = self.classroom

        return context

    def get_queryset(self):
        return self.get_queryset_student()

    def get_queryset_student(self):
        return self.model.objects.filter(classrooms=self.classroom)


class StudentListView(LoginRequiredMixin, StudentMixin, ListView):
    context_object_name = 'students'
    model = User
    template_name = 'students/student_list.html'

    def get_queryset(self):
        return super().get_queryset().order_by('first_name')


class StudentCreateView(LoginRequiredMixin, StudentMixin, CreateView):
    context_object_name = 'student'
    fields = [
        'first_name',
        'last_name',
        'email',
    ]
    model = User
    template_name = 'students/student_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        form.instance.classrooms.add(self.classroom)

        return response

    def get_success_url(self):
        return self.classroom.get_student_list_url()


class StudentDeleteView(LoginRequiredMixin, StudentMixin, DeleteView):
    context_object_name = 'student'
    model = User
    template_name = 'students/student_confirm_delete.html'

    def get_success_url(self):
        return self.classroom.get_student_list_url()


class StudentDetailView(LoginRequiredMixin, StudentMixin, DetailView):
    context_object_name = 'student'
    model = User
    template_name = 'students/student_detail.html'


class StudentUpdateView(LoginRequiredMixin, StudentMixin, UpdateView):
    context_object_name = 'student'
    fields = [
        'first_name',
        'last_name',
    ]
    model = User
    template_name = 'students/student_form.html'

    def get_success_url(self):
        return self.classroom.get_student_list_url()