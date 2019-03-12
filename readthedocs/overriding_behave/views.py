from django.shortcuts import render, redirect
from django.conf import settings


def login_sso(request):
    """
    Si se actualiza la url del administrador, tmb se debe actualiza este redirect
    esta url es la que se registra en el servidor de Oauth
    :param request:
    :return:
    """
    return redirect(settings.ADMIN_SERVER_BASE_URL + '/dj_oauth_tk_client/login/?process=login&next=/')
