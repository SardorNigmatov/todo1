from django.shortcuts import render
from rest_framework.views import APIView
from .models import ToDoModel
from .serializers import ToDoModelSerializers
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import ReadOnlyPermission, ReadOnlyDetail

# Create your views here.
class AllTask(ListAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoModelSerializers
    permission_classes = (ReadOnlyPermission,)
        # def get_queryset(self):
        #     user = self.request.user
        #     return ToDoModel.objects.filter(user=user)

class DetailTask(RetrieveAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoModelSerializers
    permission_classes = (ReadOnlyDetail,IsAuthenticated)


class CreateTask(CreateAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoModelSerializers

class UpdateTask(UpdateAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoModelSerializers
    permission_classes = (IsAuthenticated,ReadOnlyDetail)

class DeleteTask(DestroyAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoModelSerializers
    permission_classes = (IsAuthenticated,ReadOnlyDetail)





