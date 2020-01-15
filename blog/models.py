from django.db import models


# Create your models here.
class App(models.Model):
    name = models.TextField()
    title = models.TextField()
    website = models.TextField()
    abstract = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.TextField()
    identity = models.TextField()

    def __str__(self):
        return self.name
