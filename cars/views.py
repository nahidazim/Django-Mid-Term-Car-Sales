from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Car, Brand, Order, Comment
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .models import Brand

def fetch_brands(request):
    brands = Brand.objects.values_list('name', flat=True)
    return JsonResponse(list(brands), safe=False)

class CarListView(ListView):
    model = Car
    template_name = 'cars/home.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset()
        brand = self.request.GET.get('brand')
        if brand:
            queryset = queryset.filter(brand__name=brand)
        return queryset

class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            car = self.get_object()
            if car.quantity > 0:
                Order.objects.create(user=request.user, car=car)
                car.quantity -= 1
                car.save()
                return redirect('order-history')
        return redirect('login')

@method_decorator(login_required, name='dispatch')
class OrderHistoryView(ListView):
    model = Order
    template_name = 'cars/order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

def add_comment(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        Comment.objects.create(car=car, name=name, text=text)
    return redirect('car-detail', pk=pk)
