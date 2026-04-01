from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TodoItem
from .serializers import TodoSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def todo_list(request):    
    print(type(request.data))
    if request.method == 'GET':
        todos = TodoItem.objects.all()
        serializer = TodoSerializer(todos, many= True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TodoSerializer(data= request.data)
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(['PATCH', 'DELETE'])
def todo_detail(request, pk):
    todo = TodoItem.objects.get(id= pk)

    if request.method == 'PATCH':
          serializer = TodoSerializer(todo, data= request.data, partial= True)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=400)
     
    if request.method == 'DELETE':
         todo.delete()
         return Response({'message': 'Deleted'})