from django.conf.urls import url

from .views import (
    StatusAPIView,
    StatusAPIDetailView,
    # StatusDetailAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView
)

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view()),
    # url(r'^(?P<pk>\d+)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/delete/$', StatusDeleteAPIView.as_view()),
]

# Starts With
# /api/status/ -> List
# /api/status/create -> Create
# /api/status/<id>/ -> Detail
# /api/status/<id>/update -> Update
# /api/status/<id>/delete/ -> Delete

# Ends with
# /api/status/ -> List -> CRUD
# /api/status/1/ -> Detail -> CRUD

# Final
# /api/status/ -> CRUD & LS
