
from django.contrib import admin
from django.urls import path, include
from .views import hello, articles, fname, fname2
from django.conf import settings
from django.conf.urls.static import static
from clients import urls as clients_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('articles/<int:year>/', articles),
    path('pessoa/<str:nome>', fname2),
    path('person/', include(clients_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
