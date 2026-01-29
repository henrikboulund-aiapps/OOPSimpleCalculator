from CalcModes import CalcMode

class CalcEngine:
    def __init__(self, mode: CalcMode, num1: int, num2: int):
        self.mode = mode
        self.num1 = num1
        self.num2 = num2

    def calculation(self) -> float:
        match self.mode:
            case 1:
                return self.num1 + self.num2
            case 2:
                return self.num1 - self.num2
            case 3:
                return self.num1 * self.num2
            case 4:
                return self.num1 / self.num2
        return None