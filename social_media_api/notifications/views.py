from django.shortcuts import render
from .models import Notification
from rest_framework import generics
from .serializers import NotificationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

class NotificationView(generics.GenericAPIView):

    def get(self,request):

        '''
        notifications : actor : request.user
                        recipient: post.author , comment.author 
                        verb: any action 
                        target : comment post 

        '''
        try: 
             notifications = Notification.objects.get(actor=request.user)
        except Notification.DoesNotExist:
                raise NotFound(detail='there is no notifications',code=status.HTTP_404_NOT_FOUND)
        serializer = NotificationSerializer(notifications)
        if serializer:
            return Response(serializer.data)
        

    
