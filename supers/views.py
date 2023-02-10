from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupersSerializer
from .models import Super


@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        
        super_type = request.query_params.get('type')
        queryset = Super.objects.all ()
        if super_type:
            queryset = queryset.filter(super_type__type=super_type)    
            serializer = SupersSerializer(queryset, many = True)
            return Response(serializer.data)
        else:
            heroes = Super.objects.filter(super_type = 1)
            villains = Super.objects.filter(super_type = 2)
            heroes_serializer = SupersSerializer (heroes, many = True)
            villains_serializer = SupersSerializer (villains, many = True)
            custom_response_dict = {
                'Heroes': heroes_serializer.data,  
                'Villains': villains_serializer.data
            }
            return Response(custom_response_dict)

    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid (raise_exception=True)
        serializer.save ()
        return Response (serializer.data, status=status.HTTP_201_CREATED)

@api_view (['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET': 
        serializer = SupersSerializer(super)
        return Response (serializer.data)
    elif request.method == 'PUT':  
        serializer = SupersSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)