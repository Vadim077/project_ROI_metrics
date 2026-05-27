def calculate_roi(revenue: float, cost: float) -> float:
    if cost < 0:
        raise ValueError("Cost cannot be negative")
    if cost == 0:
        return 0.0
    return (revenue - cost) / cost * 100

def calculate_cr(leads: int, clicks: int) -> float:
    if clicks < 0 or leads < 0:
        raise ValueError("Clicks and leads cannot be negative")
    if clicks == 0:
        return 0.0
    return (leads / clicks) * 100

