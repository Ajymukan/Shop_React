
from django.shortcuts import render
from .models import * 
from .serializer import *
from  rest_framework import generics , mixins

from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination


from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated

class ProductsPagination (PageNumberPagination):
    page_size =  2 
    page_size_query_param = 'page_size'
    max_page_size = 10000



class ProductsAPIlist(generics.ListAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields = ('name','descriptions', 'size')


    pagination_class = ProductsPagination


class BrandAPIlist(generics.ListAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields = ('name',)


class CartAPIlist(generics.ListAPIView,mixins.CreateModelMixin,GenericAPIView):

    queryset = Cart.objects.all()
    serializer_class = Carterializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields = ('price',)
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        return self.create(request, *args,**kwargs)
    



class CartList(generics.ListAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,GenericAPIView):

    queryset = Cart.objects.all()
    serializer_class = Carterializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    permission_classes = [IsAuthenticated]
    search_fields = ('price',)

    def get(self,request,*args,**kwargs):
        return self.retrieve(request, *args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request, *args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args,**kwargs)
    


class OrderAPIlist(generics.ListAPIView,mixins.CreateModelMixin,GenericAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    permission_classes = [IsAuthenticated]
    search_fields = ('quant', )

    def post(self,request,*args,**kwargs):
        return self.create(request, *args,**kwargs)
    

class OrderList(generics.ListAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    permission_classes = [IsAuthenticated]
    search_fields = ('quant', )

    def get(self,request,*args,**kwargs):
        return self.retrieve(request, *args,**kwargs)
    
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args,**kwargs)







class CommentAPIlist(generics.ListAPIView,mixins.CreateModelMixin,GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields = ('name',)

    def post(self,request,*args,**kwargs):
        return self.create(request, *args,**kwargs)
    




class CommentList(generics.ListAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields = ('name',)

    def get(self,request,*args,**kwargs):
        return self.retrieve(request, *args,**kwargs)
    
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args,**kwargs)






