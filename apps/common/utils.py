from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def t_pay_exception_handler(exc, context):

    response = exception_handler(exc, context)
    if isinstance(exc, ValueError):
        content = {'detail': '{}'.format(exc.args)}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    elif isinstance(exc, KeyError):
        content = {'detail': '{}'.format(exc.args)}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    return response
