from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    length = models.PositiveIntegerField()
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    creator = models.ManyToManyField('Director', related_name='movies')
    # image = models.ImageField(upload_to="", blank=True, null=True)
    # avg_rating = models.ManyToManyField('User')

    def __str__(self):
        return self.name

class Director(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(blank=True, null=True)
    films = models.ManyToManyField('Movie', related_name='director', blank=True)

    def __str__(self):
        return self.fname + ' ' + self.lname

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    # rating = models.ManyToManyField('Movie')
