class Item:
    def __init__(self, name: str, color: str, price: int):
        self.name = name
        self.color = color
        self.price = price

    def is_red(self):
        return "RED" if self.color.lower() is 'red' else "NOT RED"
