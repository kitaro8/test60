from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    RMS = models.CharField(max_length=100)
    lu1 = models.CharField(max_length=100)
    lu2 = models.CharField(max_length=100)
    Latitude = models.CharField(max_length=100)
    Longitude = models.CharField(max_length=100)
    Depth = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    Gap = models.CharField(max_length=100)
    Magnitude = models.CharField(max_length=100)
    Magnitudew = models.CharField(max_length=100, blank=True)
    Region = models.CharField(max_length=100)
    image = models.ImageField(default='default1.jpg', upload_to='image_maps')
    station = ArrayField(models.CharField(max_length=200), blank=True)
    comp = ArrayField(models.CharField(max_length=200), blank=True)
    DIS = ArrayField(models.CharField(max_length=200), blank=True)
    AZM = ArrayField(models.CharField(max_length=200), blank=True)
    ARR_TIME = ArrayField(models.CharField(max_length=200), blank=True)
    RES = ArrayField(models.CharField(max_length=200), blank=True)
    PHASE = ArrayField(models.CharField(max_length=200), blank=True)
    file = models.FileField(upload_to='data')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)



    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return str(self.RMS)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Focal(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    file = models.FileField(upload_to='focal')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('focal_detail', kwargs={'pk': self.pk})


class Report(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    file = models.FileField(upload_to='report')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('report', kwargs={'pk': self.pk})