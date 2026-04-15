def calculate_premium(base_rate: float, ncb_years: int, vehicle_multiplier: float) -> float:
    """
    Calculates the insurance premium based on the base rate, NCB years, and vehicle multiplier.
    """
    # Apply NCB discount
    if ncb_years >= 4:
        ncb_discount = 0.50
    elif ncb_years == 3:
        ncb_discount = 0.40
    elif ncb_years == 2:
        ncb_discount = 0.30
    elif ncb_years == 1:
        ncb_discount = 0.20
    else:
        ncb_discount = 0.0

    premium_after_ncb = base_rate * (1 - ncb_discount)

    # Apply vehicle multiplier
    final_premium = premium_after_ncb * vehicle_multiplier

    return round(final_premium, 2)
