from django.contrib import admin
from . models import Category,News

@admin.register(Category)
class category (admin.ModelAdmin):
    list_display =("id","name")


@admin.register(News)
class News (admin.ModelAdmin):
    list_display = ("id","title","content","image","category","pub_date","created_by","created_at",'image_link')

