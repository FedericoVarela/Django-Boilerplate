from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="{{ project_name }}/index.html"))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]