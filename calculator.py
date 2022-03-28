class Calculator:
    def __init__(self) -> None:
        pass

    def adder(self, input1, input2):
        addNum = input1 + input2
        return addNum

    def subtractor(self, input1, input2):
        subNum = input1-input2
        return subNum

    def multiplier(self, input1, input2):
        mulNum = input1 * input2
        return mulNum

    def divider(self, input1, input2):
        divNum = input1/input2
        return divNum

    def clear(self, input1, input2):
        input1 = 0
        input2 = 0
        return input1, input2

calculator = Calculator()
input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: \n"))

print(str(input1) + " + " + str(input2) + " = " + str(calculator.adder(input1, input2)) + "\n")
print(str(input1) + " - " + str(input2) + " = " + str(calculator.subtractor(input1, input2)) + "\n")
print(str(input1) + " * " + str(input2) + " = " + str(calculator.multiplier(input1, input2)) + "\n")
print(str(input1) + " / " + str(input2) + " = " + str(calculator.divider(input1, input2)) + "\n")
calculator.clear(input1, input2)
print("Numbers have been reset to 0.\n")


