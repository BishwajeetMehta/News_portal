from django.contrib import admin
from . models import Category,News,Ads,SystemSetting,Mission,Vision,services,Member,Contact

@admin.register(Category)
class category (admin.ModelAdmin):
    list_display =("id","name","display_in_home")


@admin.register(News)
class News (admin.ModelAdmin):
    list_display = ("id","title","content","image","category","pub_date","created_by","views","created_at",'image_link')

@admin.register(Ads)
class Ads(admin.ModelAdmin):
    list_display= ("id","title","banner","position")

@admin.register(SystemSetting)
class SystemSetting(admin.ModelAdmin):
    list_display = ("id","name","address","phone","email","logo","salogon")

@admin.register(Mission)
class Mission(admin.ModelAdmin):
    list_display= ("id","title","description","created_at")

@admin.register(Vision)
class Vision(admin.ModelAdmin):
    list_display= ("id","title","description","created_at")

@admin.register(services)
class Services(admin.ModelAdmin):
    list_display= ("id","title","description","created_at")

@admin.register(Member)
class Member(admin.ModelAdmin):
    list_display = ("id","name","email","phone","post","image")

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display=("Sender","sender_email","subject","message")
