from django.contrib.auth import authenticate,get_user_model
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,viewsets,permissions
from .serializer import RegisterSerializer
from rest_framework.decorators import action

User = get_user_model()
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            serializer = TokenObtainPairSerializer(data=request.data)
            is_superuser = user.is_superuser
            # token, _ = Token.objects.get_or_create(user=user)
            serializer.is_valid(raise_exception=True)
            return Response({'token': serializer.validated_data, 'is_supseruser':is_superuser, 'statusCode':status.HTTP_200_OK}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.permissions import IsAuthenticated

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request):
        user = request.user
        if user:
        # The request.user will be set to the current user based on the JWT token
          serializer = RegisterSerializer(request.user)
          return Response({'userProfile': serializer.data,'isSuperuser': user.is_superuser,   'statusCode':status.HTTP_200_OK}, status=status.HTTP_200_OK )
        else:
           raise Http404


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAdminUser] 
    
    @action(detail=False, method=['post'])
    def custom_create(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            # No data found, returning 401 Unauthorized
            return Response({"detail": "No data found."}, status=status.HTTP_401_UNAUTHORIZED)

        page = self.paginate_queryset(queryset)
        if page is not limited:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        serializer= self.get_serializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)