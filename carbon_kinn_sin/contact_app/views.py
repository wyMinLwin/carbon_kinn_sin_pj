from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .serializers import ContactMessageSerializer, ReportSerializer
from .models import Report
from django.core.mail import send_mail

def send_email(subject, message, sender, recipient):
    send_mail(
        subject,
        message,
        sender,
        [recipient],
        fail_silently=False,
    )

class ContactMessageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            name = f"New Contact Message from {serializer.validated_data['name']}"
            message = serializer.validated_data['message']
            sender = serializer.validated_data['email']
            recipient = 'waiyanminlwin421@gmail.com' 
            
            send_email(name, message, sender, recipient)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportCreateView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]  

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  
        
        image = f"New Report from {serializer.validated_data['image']}"
        comment = serializer.validated_data['comment']
        sender = serializer.validated_data['email']
        recipient = 'waiyanminlwin421@gmail.com'
        
        send_email(image, comment, sender, recipient)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
