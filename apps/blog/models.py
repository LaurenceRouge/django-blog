from django.db import models


class Category(models.Model):
    category_text = models.CharField(max_length=200)
    def __str__(self):
        return self.category_text


class Article(models.Model):
    article_title = models.CharField(max_length=200, default="Titre")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.article_text
