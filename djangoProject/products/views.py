from uuid import RESERVED_FUTURE
from django.shortcuts import render
from products.models import Mobiles
from rest_framework.views import APIView
from rest_framework.response import Response
from products.serializers import ProductSerializer,MobileSerializer

# Create your views here.
class ProductsView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        if "brand" in request.query_params:
            qs=qs.filter(brand=request.query_params.get("brand"))
        if "band" in request.query_params:
            qs=qs.filter(band=request.query_params.get("band"))
        if "price_lt" in request.query_params:
            qs=qs.filter(price_lte=request.query_params.get("price_lt"))



        serializer=MobileSerializer(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        # serializer=ProductSerializer(data=request.data)
        # if serializer.is_valid():
        #     Mobiles.objects.create(**serializer.validated_data)
        #     return Response(data=serializer.data)
        # else:
        #     return Response(data=serializer.errors)
class ProductDetailView(APIView):
    def get(self,request,*args,**kw):
        id=kw.get("id")
        qs=Mobiles.objects.filter(id=id)
        serializer=MobileSerializer(qs,many=True)
        return Response(data=serializer.data)

    def delete(self,request,*args,**kw):
        id=kw.get("id")
        Mobiles.objects.filter(id=id).delete()
        return Response(data="deleted")

    def put(self,request,*args,**kw):
        id=kw.get("id")
        obj=Mobiles.objects.get(id=id)
        serializer=MobileSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        # id=kw.get("id")
        # serializer=ProductSerializer(data=request.data)
        # if serializer.is_valid():
        #     Mobiles.objects.filter(id=id).update(**serializer.validated_data)
        #     return Response(data=serializer.data)
        # else:
        #     return Response(data=serializer.errors)