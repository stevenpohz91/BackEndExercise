from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer




class ProfileList(APIView):
    def get(self, request):
        username = Profile.objects.all()
        serializer = ProfileSerializer(username, many=True)
        return Response(serializer.data)


    def post(self):
        pass



# class ProfileListTry(generics.ListCreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

# class ProfileDetailTry(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer