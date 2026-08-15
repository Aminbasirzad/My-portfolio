from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
# Create your models here.

class About(models.Model):
  name = models.CharField(max_length=100)
  title = models.CharField(max_length=200)
  description = models.TextField()
  image = models.ImageField(upload_to='about/')
  quote = models.TextField()

  def __str__(self):
    return self.title

class Resume(models.Model):
  birth_date = models.DateField()
  phone = models.CharField(max_length=15, validators=[RegexValidator(r'^09\d{9}$')])
  city = models.CharField(max_length=100)
  email = models.EmailField()
  education = models.CharField(max_length=120)
  created_at = models.DateTimeField(auto_now_add=True)
  github = models.URLField(
    blank=True,
    null=True
  )

  def age(self):
    today = timezone.now().date()
    years = today.year - self.birth_date.year
    if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
      years -= 1
    return years

  def __str__(self):
    return f"{self.name} - {self.education}"


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