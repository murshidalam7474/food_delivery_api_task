from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Organization, Pricing
from .services import PriceCalculator
def default_view(request):
    return JsonResponse({"message": "This is the default view."})

@csrf_exempt
@require_POST
def calculate_price(request):
    data = json.loads(request.body.decode('utf-8'))

    try:
        organization = Organization.objects.get(id=data['organization_id'])
    except Organization.DoesNotExist:
        return JsonResponse({"error": f"Organization with ID {data['organization_id']} not found."}, status=400)

    try:
        total_price_cents = PriceCalculator.calculate_price(
            organization=organization,
            item_type=data['item_type'],
            zone=data['zone'],
            total_distance=data['total_distance']
        )['total_price']  # Extract 'total_price' from the service response
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"total_price": total_price_cents})
