from django.shortcuts import render
from django.http.response import JsonResponse
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes


class test(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        bd = DB.objects.all()
        serializer = DBSerializer(bd, many=True)
        return Response(serializer.data)

class test2(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        bd = DB.objects.all()
        serializer = DBSerializer(bd, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retest1(request, format=None):
    bd = DB.objects.all()
    serializer = DBSerializer(bd, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def retest2(request, format=None):
    bd = DB.objects.all()
    serializer = DBSerializer(bd, many=True)
    return Response(serializer.data)

