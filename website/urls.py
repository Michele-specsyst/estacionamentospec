from django.urls import path, include, re_path
from .views import home, contato, servicos, sobre, planos


urlpatterns = [
    path(r'', home, name='website_home'),
    path(r'contato', contato, name='website_contato'),
    path(r'servicos', servicos, name='website_servicos'),
    path(r'sobre', sobre, name='website_sobre'),
    path(r'planos', planos, name='website_planos'),
]