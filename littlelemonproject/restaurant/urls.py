from django.urls import path
from .views import MenuItemView, SingleMenuItemView, BookingViewSet

urlpatterns = [
    path('menu', MenuItemView.as_view(), name="Menu"),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name="SingleMenuItem"),
    path('booking', BookingViewSet.as_view({'post':'create', 'get':'list'}), name="Booking"),
]
