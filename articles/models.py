from django.db import models

# Create your models here.

class Article(models.Model): 
    title = models.CharField(max_length=50)
    content = models.TextField()

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    
    # 여기서 content 는 id 값 
    # 여기서 article은 article_id값 