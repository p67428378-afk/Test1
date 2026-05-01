
from backend.schemas import PremiumCalculationRequest

class PremiumCalculatorService:
    def __init__(self, base_premium: float = 500.0):
        self.base_premium = base_premium

    def calculate(self, request: PremiumCalculationRequest) -> float:
        if request.ncb_years < 0:
            raise ValueError("NCB years must be a non-negative integer.")

        ncb_discount = self._get_ncb_discount(request.ncb_years)
        premium_after_ncb = self.base_premium * (1 - ncb_discount)

        vehicle_multiplier = self._get_vehicle_multiplier(request)
        final_premium = premium_after_ncb * vehicle_multiplier

        return final_premium

    def _get_ncb_discount(self, ncb_years: int) -> float:
        if ncb_years >= 4:
            return 0.5
        if ncb_years == 3:
            return 0.4
        if ncb_years == 2:
            return 0.3
        if ncb_years == 1:
            return 0.2
        return 0.0

    def _get_vehicle_multiplier(self, request: PremiumCalculationRequest) -> float:
        # This is a simplified implementation. In a real-world scenario, this would
        # involve a more complex logic, probably involving a database lookup.
        if request.vehicle_make.lower() == "ferrari":
            return 1.6
        if request.vehicle_make.lower() == "toyota":
            return 0.8
        return 1.0
