
from backend.schemas.policy import PremiumCalculationRequest

BASE_PREMIUM = 500.0
NCB_CAP = 0.5

def calculate_premium(request: PremiumCalculationRequest) -> dict:
    ncb = min(request.ncb_tier, NCB_CAP)
    vehicle_multiplier = request.vehicle_details.get("multiplier", 1.0)

    premium_after_ncb = BASE_PREMIUM * (1 - ncb)
    final_premium = premium_after_ncb * vehicle_multiplier

    return {
        "calculated_premium": final_premium,
        "base_premium": BASE_PREMIUM,
        "ncb_applied": ncb,
        "vehicle_multiplier_applied": vehicle_multiplier,
    }
