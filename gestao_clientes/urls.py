"""gestao_clientes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from decouple import config
from django.contrib import admin
from django.core.mail import mail_admins
from django.urls import path, include
from clientes import urls as clientes_urls
from produtos import urls as produtos_urls
from vendas import urls as vendas_urls
from home import urls as home_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('', include(home_urls)),
                  path('clientes/', include(clientes_urls), name="clientes"),
                  path('produtos/', include(produtos_urls), name="produtos"),
                  path('vendas/', include(vendas_urls), name="vendas"),
                  path('login/', auth_views.LoginView.as_view(), name='login'),
                  path('admin/', admin.site.urls),
                  path('', include('django.contrib.auth.urls')),
                  path('accounts/', include('allauth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path("__debug__/", include(debug_toolbar.urls))
                  ] + urlpatterns

admin.site.site_header = "Gestão de Clientes"
admin.site.index_title = "Administração"
admin.site.site_title = "Seja bem vindo ao Gestão de Clientes"
