from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book, Member, Loan
from .serializers import BookSerializer, MemberSerializer, LoanSerializer
from rest_framework import serializers
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'author', 'genre']

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        if book.available_copies < 1:
            raise serializers.ValidationError("No copies available for this book.")
        book.available_copies -= 1
        book.save()
        
        data = self.request.data
        if 'due_date' in data:
            try:
                data['due_date'] = data['due_date'][:10]  # Extract `YYYY-MM-DD`
            except (KeyError, IndexError):
                pass
        serializer.save()

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.returned_date and instance.returned_date > instance.due_date:
            days_overdue = (instance.returned_date - instance.due_date).days
            instance.fine = days_overdue * 5  # Example fine: $5 per day
            instance.save()
    
    @action(detail=True, methods=['put'], url_path='return-book')
    def return_book(self, request, pk=None):
        loan = self.get_object()
        returned_date = request.data.get('returned_date')

        if returned_date:
            loan.returned_date = returned_date
            loan.save()
            return Response({"status": "Book returned", "returned_date": loan.returned_date}, status=200)
        else:
            return Response({"error": "Returned date is required"}, status=400)
