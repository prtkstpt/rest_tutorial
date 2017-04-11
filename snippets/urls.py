from django.conf.urls import url
from snippets.views import *
from rest_framework.schemas import get_schema_view

snippet_list = SnippetViewSet.as_view({
    'get':'list',
    'post':'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
})

user_list = UserViewSet.as_view({
    'get':'list'
})

user_detail = UserViewSet.as_view({
    'get':'retrieve'
})

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^schema/$', schema_view, name='schema'),
    
    url(r'^$', api_root),
    url(r'^snippets/$', snippet_list, name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snnippet_detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user_detail'),
]
