from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.userLogin, name="login"),
    path('register/', views.userRegister, name="register"),
    path('forgotpassword/', views.forgotPassword, name="forgot-password"),
    path('changepassword/<auth_token>',
         views.changePassword, name="change-password"),

    path('logout/', views.userLogout, name="logout"),
    path('token/', views.token_send, name="token_send"),
    path('verify/<auth_token>', views.verify, name="verify"),
    path('addproduct/', views.addProduct, name="add-product"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
