def calculate_roi(revenue: float, cost: float) -> float:
    if cost < 0:
        raise ValueError("Cost cannot be negative")
    if cost == 0:
        return 0.0
    return (revenue - cost) / cost * 100