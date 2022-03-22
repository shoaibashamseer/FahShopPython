from django.urls import path

from . import views

app_name = 'eApp'

urlpatterns = [

    path('',views.allProducts,name='allProducts'),
    path('<slug:c_slug>/',views.allProducts,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatDetail')

    ]