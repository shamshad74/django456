from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class AdditionView(APIView):
    def post(self,request,*args,**kw):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1+n2
        return Response(data=res)


class SubstractionView(APIView):
    def post(self,request,*args,**kw):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1-n2
        return Response(data=res)


class FactorialView(APIView):
    def post(self,request,*args,**kw):
        n=request.data.get("num")
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return Response(data=fact)


class PrimeView(APIView):
    def post(self,request,*args,**kw):
        n=request.data.get("num")
        flag=False
        for i in range(2,n//2):
            if i%2!=0:
                flag=True

        if flag==True:
            prime='not prime'
        else:
            prime='prime'
        return Response(data=prime)

