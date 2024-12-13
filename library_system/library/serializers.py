from rest_framework import serializers
from .models import Book, Member, Loan
from django.contrib.auth.models import User
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Member
        fields = ['id', 'user', 'address', 'phone_number']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        member = Member.objects.create(user=user, **validated_data)
        return member

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
        
    def validate_due_date(self, value):
        if isinstance(value, datetime.datetime):
            return value.date()
        return value
    
    def update(self, instance, validated_data):
        if 'returned_date' in validated_data:
            instance.returned_date = validated_data.get('returned_date', instance.returned_date)
            instance.save()
        return instance