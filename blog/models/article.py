from django.db import models
#from .category import Category

class Article(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]
        