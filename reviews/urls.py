from django.urls import path
from .views import ReviewDetail, ReviewList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", ReviewList.as_view()),
    path("<int:id>", ReviewDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)