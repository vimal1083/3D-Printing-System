from django.http import JsonResponse
from _3D_Printing_System.models import STL_file_processor
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import json
from materials.models import Materials
from models import Companies
from django.db.models import Min

@api_view(['POST'])
@permission_classes((AllowAny, ))
def available_companies(request):
    material = Materials.objects.get(pk=request.POST.get('material_id'))
    stl_file_processor = STL_file_processor()
    stl_info = stl_file_processor.get_info(request.POST.get('stl_uuid'))
    # Since info API is not working I hardcode volume value
    volume = 1000

    # filter out compannies that match the conditions
    company_with_material = Companies.objects.filter(materials=material)
    filtered_companies = map(lambda company: company.prices.values_list('companies__name').annotate(Min('price')), company_with_material)
    response = [{'name':data[0][0], 'price':data[0][1]} for data in filtered_companies]
    
    return JsonResponse({'results':  response})
