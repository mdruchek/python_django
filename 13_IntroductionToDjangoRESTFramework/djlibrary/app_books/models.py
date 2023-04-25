from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    year_birth = models.IntegerField()

    def __str__(self):
        return '{firstname} {lastname}'.format(firstname=self.firstname,
                                               lastname=self.lastname)


class Book(models.Model):
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=17)
    year_release = models.IntegerField()
    number_pages = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
