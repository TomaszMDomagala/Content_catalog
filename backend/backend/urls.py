from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from stocks import views as stockviews
from catalog import views as catalogviews

router = routers.DefaultRouter()
router.register(r'stocks', stockviews.StockView, 'stock')
router.register(r'stocktypes', stockviews.StockTypeView, 'stock-types')
router.register(r'authors', catalogviews.AuthorView, 'author')
router.register(r'genres', catalogviews.GenresView, 'genre')
router.register(r'categories', catalogviews.CategoryView, 'category')
router.register(r'categoryinstances', catalogviews.CategoryInstanceView, 'categoryInstances')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stocks/', include('stocks.urls')),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
