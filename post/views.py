from django.http import JsonResponse
from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post


def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
