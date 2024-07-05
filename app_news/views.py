from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
)

from .models import Categories, News
from .serializers import CategorySerializers, NewsListSerializers, NewsVedioSerializers


class CategoryListView(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializers


class CategoryCreateView(CreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CategoryUpdateView(RetrieveUpdateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CategoryDeleteView(DestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class NewsListView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers


class NewsCreateView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]


class NewsUpdateView(RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]


class NewsDeleteView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]


class NewsListVedioView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsVedioSerializers


class NewsVedioCreateView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsVedioSerializers
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]


class NewsVedioUpdateView(RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsVedioSerializers
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]


class NewsVedioDeleteView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsVedioSerializers
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]