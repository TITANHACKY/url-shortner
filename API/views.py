from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from API.models import ShortUrl

import random

from API.serializers import ShortUrlSerializer


def random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890'
    string = "".join([random.choice(letters) for i in range(length)])
    return string

@api_view(['GET'])
def display_url(request, short_code):
    try:
        url = ShortUrl.objects.get(short_code=short_code)
        shortUrlSerializer = ShortUrlSerializer(url)

        data = shortUrlSerializer.data
        data.pop("short_code")
        return Response(data)
    except:
        return Response({"status":"error","error":"No Matching Url Found"})

@api_view(['POST'])
def add_short_url(request):
    status = dict()
    data = request.data
    data = data.dict()
    data.pop("csrfmiddlewaretoken")
    # print(len(data))
    if(len(data)==1):
        short_code = random_string(6)
        data["short_code"] = short_code
    else:
        short_code = data["short_code"]

    shortUrlSerializer = ShortUrlSerializer(data=data)
    if (shortUrlSerializer.is_valid()):
        shortUrlSerializer.save()
        status["status"] = "success"
        status["short_code"] = short_code
    else:
        status["status"] = "error"
        status["error"] = "short url with this alias already exists."

    print(status)

    return Response(status)