from django.shortcuts import render
from .models import *
import random
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth import authenticate
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError, PermissionDenied
# Create your views here.

@swagger_auto_schema(methods=['POST'] ,
                    request_body=ItemSerializer())
@api_view(['GET','POST'])
def items(request):
    item = Item.objects.all()
    print(item)
    if request.method == 'GET':
        serializer = ItemSerializer(item, many=True)
            
        data = {
        "message":"successful",
        "data": serializer.data
        }
        
        
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        
    #   print(request.data['item_id'])
      request.data['item_id'] = random.randrange(1000000,9999999) #The form will need to put any item id the code will change it to a random number dw
      print(request.data['item_id'])

      serializer = ItemSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()

        print(serializer.data)
        data = {
                'message' : 'success',
                'data'  : serializer.data,
                
            }
        return Response(data, status=status.HTTP_202_ACCEPTED)  
    

@api_view(['GET', 'DELETE'])
def items_one(request,item_id):
    try:
        item = Item.objects.get(item_id=item_id)
    except Item.DoesNotExist:

        data = {
            'message' : 'failed',
            'error'  : f"Item with ID {item_id} does not exist."
        }
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
            
        data = {
        "message":"successful",
        "data": serializer.data
        }
        
        
        return Response(data, status=status.HTTP_200_OK)


    elif request.method == 'DELETE':
        item.delete()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    

