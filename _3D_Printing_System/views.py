from django.http import JsonResponse
from models import STL_file_processor
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import json
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny, ))
def upload_stl(request):
    processor = STL_file_processor()
    uuid = processor.upload(request.FILES['file'])    
    return JsonResponse({'uuid': uuid})

def index(request):
    return TemplateResponse(request, 'index.html', {})
