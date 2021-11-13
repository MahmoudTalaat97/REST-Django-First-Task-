from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-name',)


class Cast(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    class Meta:
        ordering = ('firstname',)


class CommonInfo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='posters')
    categories = models.ManyToManyField(Category)
    cast = models.ManyToManyField(Cast)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Movie(CommonInfo):
    pass


class Series(models.Model):
    season = models.CharField(max_length=50)

