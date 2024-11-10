from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework.exceptions import PermissionDenied

class UserCreateView(generics.CreateAPIView):
    """API view to create a new user."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """Handle user creation."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  
        user = serializer.save()  
        return Response({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'ph_num': user.ph_num
        }, status=status.HTTP_201_CREATED)

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from .models import User
from .serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    """API view to create a new user."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """Handle user creation."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  
        user = serializer.save()  
        return Response({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'ph_num': user.ph_num
        }, status=status.HTTP_201_CREATED)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Get the profile details of the logged-in user."""
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        """Update the profile of the logged-in user."""
        user = request.user
        if user.id != request.user.id:
            raise PermissionDenied("You cannot update another user's profile.")

        serializer = UserSerializer(user, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """Delete the profile of the logged-in user."""
        user = request.user

        if user.id != request.user.id:
            raise PermissionDenied("You cannot delete another user's profile.")

        user.delete()
        return Response({"detail": "Profile deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
