from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        firstname = request.data.get("firstname")
        lastname = request.data.get("lastname")
        email = request.data.get("username")
        regno = request.data.get("regno")  
        sex = request.data.get("sex")
        phone_no = request.data.get("phone_no")
        role = request.data.get("role")
        campus = request.data.get("campus")
        description = request.data.get("description")

        if not username or not password or not email:
            return Response(
                {"error": "Username, password and email are required to register a user"},
                status=status.HTTP_400_BAD_REQUEST
            )

        existing_user = User.objects.filter(username=username).first()
        if existing_user:
            return Response(
                {"error": "User with this username already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        new_user = User.objects.create_user(
            username=username,
            password=password,
            first_name=firstname,  
            last_name=lastname, 
            email=email, 
            regno=regno, 
            sex=sex, 
            phone_no=phone_no, 
            role=role, 
            campus=campus,
            description=description
        )

        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
