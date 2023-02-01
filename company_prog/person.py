class Person(object):
    def __init__(self, name, money, mood, health_rate):
        self.name: str = name
        self.money: int = money
        self.mood: str = mood
        self.health_rate: str = health_rate

    def sleep(self, hours) -> str:
        if hours == 7:
            return "happy"
        elif hours < 7:
            return "tired"
        else:
            return "Lazy"

    def eat(self, meals) -> str:
        if meals == 3:
            return str(f"{100}% hth")
        elif meals == 2:
            return str(f"{75}% hth")
        elif meals == 1:
            return str(f"{50}% hth")
        else:
            return str("Error: Un expected value in {Person -> cls} {eat -> fun}")

    def buy(self, items):
        self.money -= items * 10
        self.money = max(0, self.money)  # money can not be negative



