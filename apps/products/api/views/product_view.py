from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializer import ProductSerializer
from rest_framework.response import Response

from rest_framework import generics
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(state = True)
    
    def create(self,request):
        """
        Se crea un producto en la base de datos,este es un comentario general
        
        Este es un comentario especifico
        Otro comentario
        """
        print("Hola desde POST")
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Producto creado correctamente",
                "data":request.data
                }
            )
        return Response(serializer.errors)

    def list(self, request):
        product_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response({
            "msg":"data obtenida",
            "data":product_serializer.data
        })


# class ProductListAPIView(GeneralListAPIView):
#     serializer_class = ProductSerializer


# class ProductCreateAPIView(generics.CreateAPIView):
#     serializer_class = ProductSerializer
    
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 "message":"Producto creado correctamente",
#                 "data":request.data
#                 }
#             )
#         return Response(serializer.errors)


# class ProductRetrieveAPIView(generics.RetrieveAPIView):
#     serializer_class = ProductSerializer
    
#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state = True)


# class ProductDestroyAPIView(generics.DestroyAPIView):
#     serializer_class = ProductSerializer
    
#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state = True)
    
#     def delete(self,request,pk=None):
#         product = self.get_queryset().filter(id = pk).first()
#         if product:
#             product.state = False
#             product.save()
#             return Response({"message":"Producto eliminado correctamente","data":product.product})
#         return Response({"message":"Producto no encontrado"})



# class ProductUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = ProductSerializer
    
#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state = True)
    
#     def patch(self, request, pk=None):
#         product = self.get_queryset().filter(id = pk).first()
#         if product:
#             product_serializer = self.serializer_class(product)
#             return Response(product_serializer.data, status="200")
#         return Response({"message":"Producto no encontrado"})



# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = ProductSerializer
#     queryset = ProductSerializer.Meta.model.objects.all()



# class ProductRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
#     serializer_class = ProductSerializer
#     queryset = ProductSerializer.Meta.model.objects.all()



# class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductSerializer
    
#     def get_queryset(self,pk=None):
#         if pk is None:
#             return self.get_serializer().Meta.model.objects.filter(state=True)
#         else:
#             return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
