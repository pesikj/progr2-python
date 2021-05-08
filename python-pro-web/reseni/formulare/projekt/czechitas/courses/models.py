from django.db import models

class Course(models.Model):
  name = models.CharField(max_length=100)
  start = models.DateTimeField()
  end = models.DateTimeField()
  description = models.CharField(max_length=1000)
  price = models.IntegerField()

class Branch(models.Model):
  name = models.CharField(max_length=100)
  founded_on = models.DateField() # nebo DateTimeField
  email = models.CharField(max_length=50)
  head_count = models.IntegerField()

class Person(models.Model):
  # Může být i jedno pole name
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  # příklad dalšího pole
  mobile_number = models.CharField(max_length=100, blank=True, null=True)
  active = models.BooleanField(default=False)

class Application(models.Model):
  email = models.CharField(max_length=100)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  motivation = models.TextField(blank=True, null=True)
  course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
  