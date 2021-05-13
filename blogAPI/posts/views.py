from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import generics, permissions
# from permissions import IsAuthorOrReadOnly
from posts.models import Post
from posts.serializers import PostSerializer, UserSerializer


class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
