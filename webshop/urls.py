"""webshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path , include
from django.conf.urls import  include
from aplikacija import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('svipro/<str:idp>/<str:idk>/<str:idpk>', views.single_pro),
    path('register/', views.registration_view),
    path('login/', views.login_view),
    path('logout/', views.logoOut_view),
    path('adminViews/', views.adminViews),
    path('pc/', views.creat_proiz),
    path('izlistavanje/', views.izlistavanje_proiz),
    path('izlistavanje/update/<str:pk>/<int:ik>/<str:iko>', views.editProduct),
    path('izlistavanje/delete/<int:proi_id>', views.delete_proiz),
    path('category/<int:idc>', views.wiew_category),
    path('podkategorija/<int:idom>', views.podkategorijaWiwe),
    path('shoppingCart/', views.shoppCart),
    path('slideShow/', views.slideShow),
    path('shopCart/<int:idsc>', views.shopCart),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
    path('set-new-password/<uidb64>/<token>',views.SetNewPasswordView.as_view(),name='set-new-password'),
    path('request-reset-email/',views.RequestResetEmailView.as_view(),name='request-reset-email'),
    path('shoppingCart/delete/<int:shop_id>', views.delete_shopCart),
    path('search/', views.trazi ,name='search'),
    path('adminSearch/', views.adminTrazi ,name='adminSearch'),
    path('reklama1/', views.reklama1),
    path('reklama2/', views.reklama2),
    path('tables/', views.table),
    path('phome/<str:cijena>', views.HomePageView.as_view() , name='phome'),
    path('charge/<str:cijena>', views.charge, name='charge'),
    path('custom/', views.custom, name='custom'),
    path('kontakt/', views.kontakt, name='custom'),
    path('<int:idscp>', views.updateKart, name='updateK'),
    path('messages/', views.mesages, ),
    path('about/', views.about, ),
]

