

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .services import authenticate

class AuthView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        token = authenticate(request.data['username'], request.data['password'])

        if token == '':
            return Response(
                {'status': 0, 'detail': 'Wrong username or password'},
                status=status.HTTP_403_FORBIDDEN
            )
        return Response({
            'status': 1,
            'token': token
        })


class VarifyView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        print(request.user, request.company)
        return Response({'status': 1})