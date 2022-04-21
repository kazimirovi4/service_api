from rest_framework import generics
from .models import JobList
# from .permissions import IsSuperUserOrReadOnly
from .serializers import JobListSerializer

class JobListList(generics.ListCreateAPIView):
    queryset = JobList.objects.all()
    serializer_class = JobListSerializer

class JobListDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsSuperUserOrReadOnly,)
    queryset = JobList.objects.all()
    serializer_class = JobListSerializer