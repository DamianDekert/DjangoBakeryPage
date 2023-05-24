from django.urls import path
from .views import MainSite, PrivacyPolicy

urlpatterns = [
    path("", MainSite.as_view(), name="main-site"),
    path("privacy_policy", PrivacyPolicy.as_view(), name="privacy_policy"),

]
