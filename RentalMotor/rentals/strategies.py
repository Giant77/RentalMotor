from datetime import timedelta

class PricingStrategy:
    def calculate(self, vehicle, start, end):
        raise NotImplementedError

class DailyStrategy(PricingStrategy):
    def calculate(self, vehicle, start, end):
        days = (end.date() - start.date()).days or 1
        return vehicle.price_per_day * days

class HourlyStrategy(PricingStrategy):
    def calculate(self, vehicle, start, end):
        hours = int((end - start).total_seconds() / 3600) or 1
        # assume price_per_day / 24
        return (vehicle.price_per_day / 24) * hours

class PromoWeekendStrategy(PricingStrategy):
    def calculate(self, vehicle, start, end):
        # simplified: 10% off if booking includes Saturday or Sunday
        base = DailyStrategy().calculate(vehicle, start, end)
        if start.weekday() in (5,6) or end.weekday() in (5,6):
            return base * 0.9
        return base
