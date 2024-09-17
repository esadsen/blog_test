from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True)
    article_image=models.ImageField(blank=True,null=True,verbose_name="Add image to the article")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-created_date']