from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Form
from .serializers import FormSerializer
class FormAPI(APIView):

    def get(self, request):
        return Response({'status' : True, 'message': 'GET method called'})

    def post(self, request):
        try:
            data = request.data
            user = User.objects.first()
            form = Form().create_blank_form(user)
            serializer = FormSerializer(form)
            return Response({
                'status':True,
                'message': 'form created successfully',
                'data':serializer.data
            })

        except Exception as e:
            return Response({
                'status':False,
                'message': 'something went wrong',
                'data':{}
            })