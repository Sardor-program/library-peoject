from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
 
from rest_framework.views import APIView

from rest_framework import generics, status



#class BookListApiView(generics.ListAPIView):
#   queryset = Book.objects.all()
#   serializer_class = BookSerializer

class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f'Return {len(books)} books',
            "books": serializer_data
        }
        return Response(data)
    

class BookDetailApiView(generics.RetrieveAPIView):
      queryset = Book.objects.all()
      serializer_class = BookSerializer


#class BookDeleteApiView(generics.DestroyAPIView):
 #   queryset = Book.objects.all()
  #  serializer_class = BookSerializer


class BookDeleteApiView(APIView):
   
        def get(self, request, pk):
          try:

                    book = Book.objects.get(id=pk)
                    serializer_data = BookSerializer(book).data

                    data = {
                        'satatus':'Successfuly',
                        'data':serializer_data
                    }
                    return Response(data)
          except Exception:
                    return Response({
                        'status':'False',
                        'message':'Book is not found', 
                        }, status=status.HTTP_404_NOT_FOUND
                        )

class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#class BookCreateApiView(generics.CreateAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer    

class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': f'Books are saved in database',
                'books':data
            }
            return Response(data)
        else:
            Response(
                {
                    'status':'False',
                    'message': 'Serialized is not found'
                }, status=status.HTTP_404_NOT_FOUND
            )    


class BookUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {
                'status':True,
                'message': f'Book {book_saved} update  successfuly'
            }
        )    



class BookListCeateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUptadeDeleteView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer    


class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#function based view in DRF
@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)