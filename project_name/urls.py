from django.contrib import admin
from django.urls import path, include
from decouple import config
from django.views.generic import TemplateView

DEBUG = config("DEBUG")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="{{ project_name }}/index.html"))
]

if DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]