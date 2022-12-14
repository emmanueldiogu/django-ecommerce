from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
import debug_toolbar

admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playgorund/', include('playground.urls')),
    path('store/', include('store.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('__debug__/', include(debug_toolbar.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
