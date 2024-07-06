from .models import SystemSetting,Ads,News
def system_data_processor(request):
    system_setting = SystemSetting.objects.first()
    ads = Ads.objects.all()
    news =News.objects.all().order_by('-views')[16:19]
    return {'system_setting':system_setting,'ads':ads,'newss':news}