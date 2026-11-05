from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from turf_management.models import Turf
from turf_management.serializers import TurfSerializer

from datetime import datetime

class TurfListCreateView(APIView):

    def get(self,request):

        qs = Turf.objects.all()

        serializer_instance = TurfSerializer(qs,many=True)

        return Response(serializer_instance.data)


    def post(self,request):

        form_data = request.data

        
        serializer_intance = TurfSerializer(data=form_data)

        if serializer_intance.is_valid():
            
            serializer_intance.save()#create
          
            return Response(serializer_intance.data)

        else:

            return Response(serializer_intance.errors)




class TurfRetrieveUpdateDeleteView(APIView):

    def get(self,request,pk=None):

        qs = Turf.objects.get(id=pk)

        serialzer_instance = TurfSerializer(qs)

        return Response(serialzer_instance.data)

    def put(self,request,pk=None):

        turf_object = Turf.objects.get(id=pk)

        form_data = request.data

        serializer_instance = TurfSerializer(data=form_data,instance=turf_object)

        if serializer_instance.is_valid():
            
            serializer_instance.save()#update

            return Response(serializer_instance.data)

        else:
            return Response(serializer_instance.errors)


    def delete(self,request,pk=None):

        Turf.objects.get(id=pk).delete()

        return Response({"message":"deleted..."})