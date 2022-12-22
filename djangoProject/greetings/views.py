from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
class GoodMorningView(APIView):
    def get(self,request,*args,**kw):
        return Response(data="good morning")

class GoodNightView(APIView):
    def get(self,request,*args,**kw):
        return Response(data="good night")