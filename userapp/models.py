from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='movie', blank=True)
    description = models.TextField()
    release_date = models.DateField()
    actors = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trailer_link = models.URLField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.title)



class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return '{}'.format(self.movie)








