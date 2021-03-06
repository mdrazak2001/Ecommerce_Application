from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.buyer, name="buyer"),
    path('verifyorder/<str:pk>', views.VerfiyOrderCompletion, name="verify-order")
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
