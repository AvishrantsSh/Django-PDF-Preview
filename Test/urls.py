from django.urls import path
from Test.views import ResultList

urlpatterns = [
    path("list/", ResultList, name="list"),
]
