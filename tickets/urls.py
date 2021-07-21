from django.urls import path
from .views import TicketListView, TicketDetailView, TicketCreateView, TicketUpdateView, TicketDeleteView

app_name = 'tickets'

urlpatterns = [
    path('', TicketListView.as_view(), name='all-tickets'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket_details'),
    path('<int:pk>/update/', TicketUpdateView.as_view(), name='ticket_update'),
    path('<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
    path('create/', TicketCreateView.as_view(), name='ticket_create')
]