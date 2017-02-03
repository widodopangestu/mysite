"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from mysite.views import hello, home, current_datetime, hours_ahead, template_time, template2_time, render_time, include_time, extends_time, extends_hours_ahead, display_meta, contact
from mysite import views as v1

urlpatterns = [
    url(r'^$', v1.home),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', v1.hello),
    url(r'^time/$', v1.current_datetime),
    url(r'^current-time/$', v1.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', v1.hours_ahead),
    url(r'^template-time/$', v1.template_time),
    url(r'^template2-time/$', v1.template2_time),
    url(r'^render-time/$', v1.render_time),
    url(r'^include-time/$', v1.include_time),
    url(r'^extends-time/$', v1.extends_time),
    url(r'^extends-plus/(\d{1,2})/$', v1.extends_hours_ahead),
    url(r'^meta/$', v1.display_meta),
    url(r'^contact/$', v1.contact),
    url(r'^books/', include('books.urls')),
]
