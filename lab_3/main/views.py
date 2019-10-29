from django.shortcuts import render
from django.http import JsonResponse
import os
import platform
from datetime import datetime


def main(request):
    return render(request, 'main.html', {'parameter': "test"})



def health(request):
    response = {'date': datetime.today(),
                'current_page': request.path,
                'server_info': {
                    'system': platform.system(),
                    'version': platform.version(),
                    'release': platform.release(),
                    'network name': platform.node(),
                    'machine': platform.machine(),
                    'processor': platform.processor()
                },
                'client_info': request.META['HTTP_USER_AGENT']}
    return JsonResponse(response)