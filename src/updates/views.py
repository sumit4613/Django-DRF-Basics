from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.shortcuts import render
from django.views.generic import View
from .models import Update
from api.mixins import JsonResponseMixin
import json


# def detail_view(request):
#     return HttpResponse(get_template().render({}))  # return JSON Data


def json_example_view(request):
    """
    URI -> for a REST API
    GET -> Retrieve
    """
    data = {"count": 100, "content": "some new content"}
    json_data = json.dumps(data)
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type="application/json")


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {"count": 100, "content": "some new content"}
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {"count": 100, "content": "some new content"}
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = serialize("json", [obj, ], fields=("user", "content"))
        # data = {"user": obj.user.username, "content": obj.content}
        json_data = data
        return HttpResponse(json_data, content_type="application/json")


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        data = serialize("json", qs, fields=("user", "content"))
        # data = {"user": obj.user.username, "content": obj.content}
        json_data = data
        return HttpResponse(json_data, content_type="application/json")
