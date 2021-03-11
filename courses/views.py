from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import CourseSerializer
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

# @api_view(['GET'])
# def apiCourse(request):
#     return Response("API BASE POINT")

class CourseApiListView(APIView):

    permission_classes = (IsAuthenticated, )
    def get(self, request, *args, **kwargs):
        courses = Courses.objects.all()
        serializers = CourseSerializer(courses, many=True)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializers.data)

# @api_view(['GET'])
# def apiList(request):
#     courses = Course.objects.all()
#     serializers = CourseSerializer(courses, many=True)
#     return Response(serializers.data)

# @api_view(['GET'])
# def apiDetail(request, slug):
#     course = Course.objects.get(slug=slug)
#     serializer = CourseSerializer(course, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def apiCreate(request):
#     serializer = CourseSerializer(data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)

# @api_view(['POST'])
# def apiUpdate(request, pk):
#     course = Course.objects.get(id=pk)
#     serializer = CourseSerializer(instance=course, data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)
