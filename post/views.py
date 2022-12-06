from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import PostSerializer, PostTitleSerializer
from .models import Post


@api_view(['GET'])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def post_detail(request, pk):
    if request.method == "GET":
        posts = Post.objects.filter(pk=pk)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def post_title_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostTitleSerializer(posts, many=True)
        return Response(serializer.data)