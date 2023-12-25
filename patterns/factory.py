# Створимо інтерфейс продукту
class Product:
    def display(self):
        pass

# Створимо класи-спадкоємці, які реалізують продукти
class ConcreteProduct1(Product):
    def display(self):
        return "ConcreteProduct1"

class ConcreteProduct2(Product):
    def display(self):
        return "ConcreteProduct2"

# Створимо фабрику для створення продуктів
class Factory:
    def create_product(self, product_type):
        if product_type == 1:
            return ConcreteProduct1()
        elif product_type == 2:
            return ConcreteProduct2()
        else:
            raise ValueError("Unsupported product type")

# Приклад використання фабрики
factory = Factory()

product1 = factory.create_product(1)
print(product1.display())  # Виведе: ConcreteProduct1

product2 = factory.create_product(2)
print(product2.display())  # Виведе: ConcreteProduct2
