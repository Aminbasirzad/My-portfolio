from django.db import models

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  subject = models.CharField(max_length=200)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return self.name


class Skils(models.Model):
  name = models.CharField(max_length=100)
  percentage = models.PositiveBigIntegerField(default=0)

  def __str__(self):
    return self.name