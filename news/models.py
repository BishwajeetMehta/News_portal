from django.db import models

from account.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class META :
        ordering =['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name
    
class News(models.Model):
    title =models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField()
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey (User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add= True)
    image_link = models.URLField(blank=True,null=True)

    class META :
        ordering =['title']
        verbose_name = 'news'
        verbose_name_plural = 'newses'

    def __str__(self) -> str:
        return self.title