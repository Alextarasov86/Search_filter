from rest_framework import exceptions
from django.contrib.auth.models import AnonymousUser
from .services import get_user_by_token, is_token_expired, logout
from .models import *


class GetUserCompanyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'Authorization' in request.headers.keys():
            token = request.headers['Authorization'].split(' ')[1]
            user = get_user_by_token(token)

            if not user is None:
                user_company = UserCompany.objects.get(user=user)
                request.company = user_company.company

        response = self.get_response(request)

        return response

class CheckTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request,):
        if 'Authorization' in request.headers.keys():
            token = request.headers['Authorization'].split(' ')[1]
            if is_token_expired(token):
                logout(token=token)
                request.user = AnonymousUser()

        response = self.get_response(request)

        return response