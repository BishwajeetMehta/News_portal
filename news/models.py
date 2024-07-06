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
    

class Ads(models.Model):
    POSITION_CHOICES = (
    ('top', "top"),
    ('lower', "lower"),
    ('middle', "middle"),
    ('left', "left"),
    ('category_page_banner', "category_page_banner"),
)
    title = models.CharField(max_length=250)
    banner = models.ImageField()
    position = models.CharField(max_length=50,choices=POSITION_CHOICES)
    history = AuditlogHistoryField()

class SystemSetting(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    logo = models.ImageField()
    salogon = models.TextField()
    history = AuditlogHistoryField()


class Mission(models.Model):
    title = models.TextField()
    description = models.TextField()
    created_at = models.DateField(auto_now_add= True)

class Vision(models.Model):
    title = models.TextField()
    description = models.TextField()
    created_at = models.DateField(auto_now_add= True)

class services(models.Model):
    title = models.TextField()
    description = models.TextField()
    created_at = models.DateField(auto_now_add= True)

class Member(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    post = models.CharField(max_length=100)
    image = models.ImageField()


class Contact(models.Model):
    Sender = models.CharField(max_length=100)
    sender_email = models.CharField(max_length=100)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.Sender


auditlog.register(Category, serialize_data=True)
auditlog.register(News, serialize_data=True)
auditlog.register(Ads, serialize_data=True)
auditlog.register(SystemSetting, serialize_data=True)