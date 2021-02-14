
from django.contrib import admin
from django.urls import path
from crm.views import first_page, success_page
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first_page),
    path('suc', success_page, name='suc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# https://api.telegram.org/bot390769552:AAGVu-AxIWqZjkl5bExjodMrFQmC_7ZwtQY/sendMeesage?chat_id=-502671643&text=Привет