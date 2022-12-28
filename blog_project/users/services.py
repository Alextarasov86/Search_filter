from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


def authenticate(username: str, password: str) -> str:
    """
    Метод принимает логи и пароль пльзователя и пытается его авторизовать.
    Если авторизация успешна - возвращает токен пользователя.
    Если неуспешна - пустую строку.
    """
    mb = ModelBackend()
    user = mb.authenticate(
        request=None,
        username=username,
        password=password,
    )

    if user is None:
        return ''

    try:
        token = Token.objects.get(user=user)
        token.delete()
    except:
        pass

    token = Token.objects.create(user=user)

    return token.key

def logout(user=None, token=''):
    if not user is None:
        token = Token.objects.get(user=user)
    if token != '':
        token = Token.objects.get(key=token)
    token.delete()


def get_user_by_token(token: str) -> str:
    try:
        t = Token.objects.get(key=token)
    except:
        return None

    return t.user


# Возвращает оставшееся время жизни токена
def expires_in(token):
    t = Token.objects.get(key=token)
    time_elapsed = timezone.now().timestamp() - t.created.timestamp()
    left_time = settings.TOKEN_EXPIRED_AFTER_SECOND -  time_elapsed
    return left_time

# Проверяем закончилось ли время токена или нет
def is_token_expired(token):
    return expires_in(token) < 0
