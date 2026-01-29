import CalcEngine

def main() -> None:
    while True:
        print("===SIMPLE CALCULATOR===")

        print("1) Addition\n2) Subtraction\n3) Multiplication\n4) Division")

        choice: int = int(input("Enter your choice: "))

        def request_number_inputs() -> list[str]:
            number1 = int(input("Enter first number: "))
            number2 = int(input("Enter second number: "))

            list1 = [number1, number2]

            return list1

        response : list[str] = request_number_inputs()
        engine = CalcEngine.CalcEngine(choice, response[0], response[1])

        print("RESULT: ", engine.calculation())

if __name__ == "__main__":
    main()