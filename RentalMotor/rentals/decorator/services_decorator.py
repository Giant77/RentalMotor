from decimal import Decimal
from ..strategies import PricingStrategy, DailyStrategy

class RentalCost:
    def cost(self) -> Decimal:
        raise NotImplementedError

class BaseRental(RentalCost):
    def __init__(self, base_amount: Decimal):
        self._base = base_amount
    def cost(self): return self._base

class RentalDecorator(RentalCost):
    def __init__(self, rental: RentalCost):
        self._rental = rental
    def cost(self):
        return self._rental.cost()

# Add-on: Helmet
class HelmetAddon(RentalDecorator):
    def __init__(self, rental, helmet_price: Decimal):
        super().__init__(rental)
        self.helmet_price = helmet_price
    def cost(self):
        return self._rental.cost() + self.helmet_price

# Add-on: Jacket
class JacketAddon(RentalDecorator):
    def __init__(self, rental, jacket_price: Decimal):
        super().__init__(rental)
        self.jacket_price = jacket_price
    def cost(self):
        return self._rental.cost() + self.jacket_price

# Fine decorator for damage
class DamageFineDecorator(RentalDecorator):
    def __init__(self, rental, fine_amount: Decimal):
        super().__init__(rental)
        self.fine_amount = fine_amount
    def cost(self):
        # optionally, can apply penalty multipliers
        return self._rental.cost() + self.fine_amount

def compute_total(vehicle, start, end, strategy: PricingStrategy):
    return strategy.calculate(vehicle, start, end)
