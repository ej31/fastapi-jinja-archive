class Item:
    def __init__(self, name: str, color: str, price: int, state: str = "ok"):
        self.name = name
        self.color = color
        self.price = price
        self.state = state

    def is_red(self):
        return "RED" if self.color.lower() == 'red' else "NOT RED"
