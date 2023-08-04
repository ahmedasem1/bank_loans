from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path("signup", views.RegisterUserAPIView.as_view(), name="signup"),

    path("registerprovider/<uuid:uuid>/", views.RegisterProviderAPIView.as_view(), name="registerprovider"),
    path("registercustomer/<uuid:account_uuid>/", views.RegisterCustomerAPIView.as_view(), name="registercustomer"),
    path("registerpersonnel/<uuid:acc_uuid>/", views.RegisterPersonnelAPIView.as_view(), name="registerpersonnel"),
    # path("personnelloan/<uuid:acc_uuid>/", views.loan_detail.as_view(), name="personnelloan"),
    path("personnelloan/", views.loan_detail.as_view(), name="coustmerloan"),

]