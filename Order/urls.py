from django.conf.urls import include, url
from django.contrib import admin
import ezorder.urls

from background_task import tasks
tasks.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ezorder.views.get_index'),
    url(r'^ezorder/', include(ezorder.urls)),
]
