from django.contrib import admin
from .models import Category, Course, Lesson, Module


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'slug', 'owner', 'price', 'status']
    list_filter = ['status', 'owner', 'category']


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['course', 'title', 'slug']
    list_filter = ['course']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['module', 'name', 'slug']
    list_filter = ['module']
