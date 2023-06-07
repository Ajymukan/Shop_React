
from django.contrib import admin
from django.urls import path,include 

from django.conf.urls.static import static
from .settings import MEDIA_ROOT,MEDIA_URL

from django.conf.urls.i18n import i18n_patterns 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),

    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),

]

urlpatterns += i18n_patterns(
 path('api/v1/', include('rest_app.urls')),

)

urlpatterns += static(MEDIA_URL , document_root = MEDIA_ROOT)
