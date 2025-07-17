from data.fetch import fetch_price

class PortfolioManager:
    def __init__(self, positions):
        self.positions = positions

    def calculate_value(self):
        total_value = 0
        for symbol, data in self.positions.items():
            price = fetch_price(symbol)
            total_value += price * data['shares']
        return total_value
