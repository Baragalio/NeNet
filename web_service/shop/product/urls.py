from django.urls import path
from . import views



urlpatterns = [
    path('', views.list_product, name='list_product'),
    path('<slug:category_slug>/', views.list_product, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail')
]
