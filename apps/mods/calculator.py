class Calculator:
    def __init__(self) -> None:
        pass

    def add(self, num1, num2) -> int:
        result = num1 + num2
        return result
    
    def sub(self, num1, num2) -> int:
        result = num1 - num2
        return result
    
    def mul(self, num1, num2) -> int:
        result = num1 * num2
        return result
    
    def div(self, num1, num2) -> int:
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError as e:
            return f"{e}"
    
test = Calculator()
print(test.add(1,2))
print(test.sub(1,2))
print(test.mul(1,2))
print(test.div(2,0))