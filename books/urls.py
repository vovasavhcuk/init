from django.urls import path
from .views import BookDetail, BookList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", BookList.as_view()),
    path("<int:id>", BookDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)