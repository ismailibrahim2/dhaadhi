from rest_framework.response import Response
from rest_framework.decorators import api_view
from courses.models import Category, Course, Requirements, Benifits, Module, Lesson
from . import serializers


@api_view(['GET'])
def course_list(request):
    courses = Course.objects.filter(status='published')
    serializer = serializers.CourseSerializer(courses, many=True)
    return Response(serializer.data)


def category_list(request):
    categories = Category.objects.all()
    serializer = serializers.CategorySerializer(categories, many=True)
    return Response(serializer.data)
