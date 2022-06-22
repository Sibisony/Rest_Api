from urllib import response
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import EmpData
from accounts.serializers import EmpDataSerializer
# Create your views here.
@api_view(['GET'])
def Apioverview(request):
    return Response('API Calling')

@api_view(['GET'])    
def EmpList(request):
    emp=EmpData.objects.all()
    serializer=EmpDataSerializer(emp,many=True)
    return Response(serializer.data)

@api_view(['POST'])  
def Empcreate(request):
    serializer=EmpDataSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response('item added')
@api_view(['POST'])         
def Empupdate(request,pk):
    serializer=EmpData.objects.get(pk=pk)
    data=EmpDataSerializer(instance=serializer ,data=request.data)
    if data.is_valid():
        data.save()
        return Response('item updated')
@api_view(['DELETE'])
def Empdelete(request,pk):
    serializer=get_object_or_404(EmpData,pk=pk)
    serializer.delete()
    return Response('item delete')  
           