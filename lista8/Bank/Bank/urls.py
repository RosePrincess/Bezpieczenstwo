"""Bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from transfers.views import transfer_sending, transfer_confirmed, transfer_sent, transfers_history, admin_transfers_to_confirm, admin_confirm_transfer, admin_csrf_attack

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('transfer/', transfer_sending, name='transfer'),
    path('transfer_confirm/', transfer_confirmed, name='transfer_confirm'),
    path('transfer_sent/', transfer_sent, name='transfer_sent'),
    path('transfers_history/', transfers_history, name='transfers_history'),
    path('admin_transfers_to_confirm/', admin_transfers_to_confirm, name='transfers_to_confirm'),
    # path('admin_confirm_transfer/<int:transfer_id>/', admin_confirm_transfer, name='confirm_transfer'),
    url(r'^admin_confirm_transfer/(?P<transfer_id>\d+)/$', admin_confirm_transfer, name='confirm_transfer'),
    path('you_won/', admin_csrf_attack, name='atack'),
    path('', TemplateView.as_view(template_name='home.html'), name='home')
]
