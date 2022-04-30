from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path("store/", views.category_list, name="store"),
    path('category/<slug:category_list>/', views.category_list, name='category_list'),
    path('detail/<slug:product_details>/', views.product_details, name='product_details'),
]
