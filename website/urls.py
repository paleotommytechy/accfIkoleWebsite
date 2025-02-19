from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

def privacy_view(request):
    return render(request, 'privacy.html')

urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('privacy/', privacy_view, name='privacy'),
]
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
