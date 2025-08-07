from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Import all views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Core pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Student details view with slug
    path('details/<slug:slug>/', views.details, name='details'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
