from xml.etree.ElementInclude import include
from django.urls import path
from graphene_django.views import GraphQLView
from traffic_backend.schemas import schema
import traffic_backend.views as views
urlpatterns = [
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
    path('csrf/', views.get_csrf, name='api-csrf')
]