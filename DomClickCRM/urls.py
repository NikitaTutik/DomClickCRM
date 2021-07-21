from django.contrib import admin
from django.urls import path, include
from tickets.views import WelcomePageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WelcomePageView.as_view(), name='welcome_page'),
    path('tickets/', include('tickets.urls', namespace='tickets'))
]
