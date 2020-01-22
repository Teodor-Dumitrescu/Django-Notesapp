from django.conf.urls import url, include
from django.contrib import admin
#from djangonote.views import home_view
from notes.views import index_view, add_note

app_name = 'app1'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name='index'),
    url(r'^addnote/', add_note, name='addnote'),
]