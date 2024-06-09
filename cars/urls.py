from django.urls import path
from .views import CarListView, CarDetailView, OrderHistoryView, add_comment
from .views import fetch_brands

urlpatterns = [
    path('', CarListView.as_view(), name='home'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('order-history/', OrderHistoryView.as_view(), name='order-history'),
    path('car/<int:pk>/comment/', add_comment, name='add-comment'),
    path('fetch-brands/', fetch_brands, name='fetch-brands'),
]
