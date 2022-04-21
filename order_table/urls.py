from django.urls import path
from .views import JobListList, JobListDetail

urlpatterns = [
    path('<int:pk>/', JobListDetail.as_view()),
    path('', JobListList.as_view()),
]