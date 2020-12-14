from django.shortcuts import render
from home.models import Notes
from rest_framework.views import APIView
from .serilaizers import Notes_Serilaizer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# Create your views here.


class ShowUserNotes(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        note = Notes.objects.filter(user=self.request.user)
        serilazier = Notes_Serilaizer(note, many=True)
        return Response(serilazier.data)
    # post notes from here

    def post(self, request):
        serilazier = Notes_Serilaizer(data=request.data)
        if serilazier.is_valid():
            serilazier.save()
            return Response(serilazier.data, status=status.HTTP_201_CREATED)


class NotesDetailsView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication]

    def get_object(self, id):
        try:
            return Notes.objects.get(id=id)
        except Notes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        note = Notes.objects.get(id=id)

        if note.user == request.user:
            serilazier = Notes_Serilaizer(note)
            return Response(serilazier.data)
        else:
            return Response({'sucess': False, 'message': 'note not found'})

    def put(self, request, id):
        note = self.get_object(id=id)
        serializer = Notes_Serilaizer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'sucess': False, 'message': 'note not found'})

    def delete(self, request, id):
        note = self.get_object(id=id)
        if note.user == request.user:
            note.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


class Login_API_View(APIView):
    def post(self, request):
        password = request.data.get('password')
        user_name = request.data.get('user_name')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=userx)
            return Response({"success": True, "key": token.key})
        else:
            return Response({'sucess': False, 'message': 'invalid username or password', })
