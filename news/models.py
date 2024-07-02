from django.db import models

from account.models import User
from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
# Create your models here.
class Category(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    display_in_home = models.BooleanField(default=False)
    history = AuditlogHistoryField()

    class META :
        ordering =['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name
    
class News(models.Model):
    objects = None
    title =models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(blank=True,null=True)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey (User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add= True)
    image_link = models.URLField(blank=True,null=True)
    views = models.PositiveIntegerField(default=0)
    history = AuditlogHistoryField()

    class META :
        ordering =['title']
        verbose_name = 'news'
        verbose_name_plural = 'newses'

    def __str__(self) -> str:
        return self.title
    

auditlog.register(Category, serialize_data=True)
auditlog.register(News, serialize_data=True)