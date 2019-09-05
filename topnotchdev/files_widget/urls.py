try:
    from django.conf.urls.defaults import url
except:
    from django.conf.urls import url

from django.conf import settings
from .views import upload, thumbnail_url

urlpatterns = [
    url('^upload', upload, name="files_widget_upload"),
    url('^thumbnail-url', thumbnail_url, name="files_widget_get_thumbnail_url"),
]
