from django.db import models

# Create your models here.
class Movie(models.Model):
    
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('science_fiction', 'Science Fiction'),
        ('fantasy', 'Fantasy'),
    ]
    
    title = models.charField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)