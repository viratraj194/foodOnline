from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from marketplace import views as marketplaceViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('accounts.urls')),
     #cart creations 
    path('cart/', marketplaceViews.cart, name='cart'),

    path('marketplace/', include('marketplace.urls')),
    #search
    path('search/',marketplaceViews.search, name='search'),

    #checkout

    path('checkout/',marketplaceViews.checkout, name='checkout'),

    # orders
    path('orders/',include('orders.urls')),
        #virat profile
    path('virat_profile/',views.virat_profile,name='virat_profile')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
