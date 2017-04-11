
from snippets.models import Snippet
from snippets.serializers import *
from rest_framework import generics 
from django.contrib.auth.models import User

from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
        'schema': reverse('schema', request=request, format=format)
    })

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    # class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    #     queryset = Snippet.objects.all()
    #     serializer_class = SnippetSerializer
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
        
        # class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
