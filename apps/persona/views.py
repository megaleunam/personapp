from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apps.persona.serializers import UserSerializer, GroupSerializer, PersonaSerializer,EventoSerializer


from rest_framework.views import APIView

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.persona.models import Snippet,Persona,Evento
from apps.persona.serializers import SnippetSerializer

"""
title: 
Endpoint para usuarios
"""
class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given user.

    list:
    Return a list of all the existing users.

    create:
    Create a new user instance.

    put: 
    actualiza los datos del usuario

    description:
    Entidad de Usuario

    update:
    Actualización del Usuario
        
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roles to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SnipppetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    """
    Cigar resource.
    ---
    retrieve:
    Retorna un registro de Persona .

    list:
    Retorna una lista de todas las personas Existentes.

    create:
    Create una nueva instancia de Persona.

    update:
    Actualización del Usuario
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class EventoViewSet(viewsets.ModelViewSet):
    """
    Recurso de Evento.
    ---
    retrieve:
    Retorna un registro de Evento .

    list:
    Retorna una lista de todas los Eventos Existentes.

    create:
    Create una nueva instancia de Evento.

    update:
    Actualización del Evento

    delete:
    Elimina un Evento.
    
    """
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


