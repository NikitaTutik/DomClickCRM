from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from tickets.views import WelcomePageView, SignUpView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WelcomePageView.as_view(), name='welcome_page'),
    path('tickets/', include('tickets.urls', namespace='tickets')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('employees/', include('employees.urls', namespace='employees'))
]

if settings.DEBUG:
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
