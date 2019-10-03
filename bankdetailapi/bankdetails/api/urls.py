from .views import GetBankDetails
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
# from django.urls import path


urlpatterns = [
    url(r'^$', GetBankDetails.as_view(), name='get-bank-details'),
    # url(r'^api/', include('rest_framework_simplejwt.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]
