import os
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from instructors.models import Instructor


class Category(models.Model):
    name = models.CharField(max_length=90)
    slug = models.SlugField(max_length=90, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


def save_course_images(instance, filename: str):
    upload_to = 'Course Images'
    ext = filename.split('.')[-1]
    if instance.title:
        filename = '{}/{}/{}/{}.{}'.format(instance.owner.user.username,
                                           instance.category.name, instance.title, instance.title, ext)
    return os.path.join(upload_to, filename)


# class PublishManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).status

class Course(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, unique=True, null=True, blank=True)
    owner = models.ForeignKey(Instructor, on_delete=models.PROTECT)
    thumbnail = models.ImageField(upload_to=save_course_images)
    description = RichTextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=10, default='draft')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Requirements(models.Model):
    """
        What do students need to take this course.
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Benifits(models.Model):
    """
        What will students learn from this course.
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True, null=True, blank=True)
    description = RichTextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


def save_course_lessons(instance, filename: str):
    upload_to = 'Course Videos/'
    ext = filename.split('.')[-1]
    if instance.name:
        filename = '{}/{}/{}/{}/{}/{}.{}'.format(instance.module.course.owner.user.username,
                                                 instance.module.course.category.name, instance.module.course.title, instance.module.title, instance.name, instance.name, ext)
    return os.path.join(upload_to, filename)


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    video = models.FileField(upload_to=save_course_lessons)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Lesson, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
