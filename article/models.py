from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True)
    update_count = models.IntegerField(default=0) 

    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-created_date']