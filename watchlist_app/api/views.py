from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins


class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset=Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)    

class StreamPlatformAV(APIView):
    def get(self,request):
        queryset = StreamPlatform.objects.all()
        serializers = StreamPlatformSerializer(queryset, many=True)
        return Response(serializers.data)

    def post(self,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamPlatformDetailAV(APIView):
    def get(self,request,pk):
        try:
            stream=StreamPlatform.objects.get(pk=pk)
        except stream.DoesNotExist:
            return Response({'errror': "stream Does not Present"})
        
        serializer = StreamPlatformSerializer(stream)
        return Response(serializer.data)

    def put(self,request,pk):
        stream= StreamPlatform.objects.get(id=pk)
        serializer = StreamPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        stream= StreamPlatform.objects.get(id=pk)
        stream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class WatchListAV(APIView):

    def get(self,request):
        movies= WatchList.objects.all()
        serializers = WatchListSerializer(movies, many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class  WatchDetailAV(APIView):
    def get(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'errror': "Movie Does not Present"})
        
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self,request,pk):
        movie= WatchList.objects.get(id=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        movie= WatchList.objects.get(id=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         try:
#             movies= Movie.objects.all()
#         except Movie.DoesNotExist:
#             return Response({{"message": "The data does not found"}, {"status":HTTP_404_NOT_FOUND}})
#         serializers = MovieSerializer(movies, many=True)
#         return Response(serializers.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             movie= Movie.objects.get(id=pk)
#         except Movie.DoesNotExist:
#             return Response(status=status.HTTP_204_NO_CONTENT)
        
#         serializers = MovieSerializer(movie)
#         return Response(serializers.data)
  
#     if request.method == 'PUT':
        movie= Movie.objects.get(id=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

#     if request.method == 'DELETE':
        movie= Movie.objects.get(id=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


