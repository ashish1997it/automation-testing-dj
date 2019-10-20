from common.helper.response import ResponseView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class LoginView(APIView):

    @csrf_exempt
    @api_view(['POST'])
    @permission_classes((AllowAny,))
    def user_login(request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")

            if username is None or password is None:
                return ResponseView.api_response(status_code=400, status_message='error',
                                                 message=['Please provide both username and password!'])

            user = authenticate(username=username, password=password)

            if not user:
                return ResponseView.api_response(status_code=404, status_message='error',
                                                 message=['Invalid credentials!'])

            token, _ = Token.objects.get_or_create(user=user)
            request.session['user_name'] = username

            return ResponseView.api_response(message=['You are successfully logged in.'], data=[{'token': token.key}])

        except Exception as ex:
            print('ex: ', ex)
            return ResponseView.api_exception_response(status_code=400, status_message='exception', message=str(ex))

    @csrf_exempt
    @api_view(['POST'])
    @permission_classes((AllowAny,))
    def user_logout(request):
        try:
            user_name = request.session['user_name']
            user_id = User.objects.only('id').get(username=user_name).id
            instance = Token.objects.filter(user=user_id)
            instance.delete()
            return ResponseView.api_response(message=['logout successfully.'])

        except Exception as ex:
            print('ex: ', ex)
            return ResponseView.api_exception_response(status_code=400, status_message='exception', message=str(ex))

    @csrf_exempt
    @api_view(['GET'])
    @transaction.atomic
    def get_message(request):
        try:
            return ResponseView.api_response(message=['Access data successfully.'])

        except Exception as ex:
            print('ex: ', ex)
            return ResponseView.api_exception_response(status_code=400, status_message='exception', message=str(ex))
