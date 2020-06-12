"""milestone_four URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog import urls as blog_urls
from accounts import urls as accounts_urls
from products import urls as products_urls
from search import urls as search_urls
from click_and_collect import urls as click_and_collect_urls
from categories import urls as categories_urls
from faq import urls as faq_urls
from contact import urls as contact_urls
from help import urls as help_urls
from shows import urls as shows_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(products_urls)),
    path('accounts/', include(accounts_urls)),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('blog/', include(blog_urls)),
    path('search/', include(search_urls)),
    path('click_and_collect/', include(click_and_collect_urls)),
    path('categories/', include(categories_urls)),
    path('faq/', include(faq_urls)),
    path('contact_us/', include(contact_urls)),
    path('help/', include(help_urls)),
    path('shows/', include(shows_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
