from django.contrib import admin
from django.urls import path, include
from captcha import urls as captcha_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("User.urls")), 
    path("accounts/", include("allauth.urls")),
     path('captcha/', include(captcha_urls)),
]

