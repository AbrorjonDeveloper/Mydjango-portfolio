from django.shortcuts import render
from .models import Course
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
class CourseListView(ListView):
    template_name = "courses.html"
    model = Course
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    template_name = "course_detail.html"
    model = Course

class CourseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "course_create.html"
    model = Course
    fields = ['title', 'category','content','description','tutorial']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'course_update.html'
    model = Course
    fields = ['title', 'category','content','description','tutorial']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "complete_form.html"
    model = Course
    success_url = "course/list"
    fields = []

    def test_func(self):
        course = self.get_object()
        if self.request.user.is_staff:
            return True
        return False
        
def courses(request):
    return render(request, 'courses.html')
