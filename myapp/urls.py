
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.tool,name='tool'),
    # path('install',views.install,name="install"),
    path('',views.index,name='index'),
    path('app',views.app,name='app'),
    path('dele',views.dele,name='dele'),
    path('list',views.list,name='list')
    

]
