# food_delivery_app/services.py

from .models import Pricing

class PriceCalculator:
    @staticmethod
    def calculate_price(organization, item_type, zone, total_distance):
        try:
            pricing = Pricing.objects.get(
                organization=organization,
                item__type=item_type,
                zone=zone
            )
        except Pricing.DoesNotExist:
            raise ValueError("Pricing not found for the given parameters.")

        base_distance = pricing.base_distance_in_km
        base_price = pricing.fix_price
        per_km_price = (
            pricing.km_price_perishable if item_type == "perishable" else pricing.km_price_non_perishable
        )

        if total_distance <= base_distance:
            total_price = base_price
        else:
            additional_distance = total_distance - base_distance
            total_price = base_price + additional_distance * per_km_price

        # Convert total_price to cents to avoid decimal issues
        total_price_cents = round(total_price, 2) 

        return {"total_price": total_price_cents}
