import math
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from .UnaryExpression import UnaryExpression
from .MultiplicationExpression import MultiplicationExpression
from .DivisionExpression import DivisionExpression
from .AdditionExpression import AdditionExpression
from .SubtractionExpression import SubtractionExpression

class PercentExpression(UnaryExpression):
    def __init__(self, tableWidget, expression):
        super().__init__(tableWidget)
        self.expression = expression

    def calculate(self, number: float):
        result: float = None
        if isinstance(self.expression,  MultiplicationExpression):
            self.insert_scroll_table()
            result = number / 100.0 * self.expression.first_number
            self.protocol(number, 0)
            self.protocol("% of", 1)
            self.protocol(self.expression.first_number, 2)
            self.protocol("=", 3)
            self.protocol_result(result, 4)
        elif isinstance(self.expression,  DivisionExpression):
            self.insert_scroll_table()
            result = self.expression.first_number * 100.0 / number
            self.protocol("Ratio of", 0)
            self.protocol(self.expression.first_number, 1)
            self.protocol("to", 2)
            self.protocol(number, 3)
            self.protocol("=", 4)
            self.protocol_result(result, 5)
            self.protocol("%", 6)
        elif isinstance(self.expression,  AdditionExpression):
            self.insert_scroll_table()
            intermediate = number / 100.0 * self.expression.first_number
            self.protocol(number, 0)
            self.protocol("% of", 1)
            self.protocol(self.expression.first_number, 2)
            self.protocol("=", 3)
            self.protocol_result(intermediate, 4)

            self.insert_scroll_table()
            result = self.expression.first_number * (1.0 + number / 100.0)
            self.protocol(number, 0)
            self.protocol("% add-on of", 1)
            self.protocol(self.expression.first_number, 2)
            self.protocol("=", 3)
            self.protocol_result(result, 4)
        elif isinstance(self.expression,  SubtractionExpression):
            self.insert_scroll_table()
            intermediate = number / 100.0 * self.expression.first_number
            self.protocol(number, 0)
            self.protocol("% of", 1)
            self.protocol(self.expression.first_number, 2)
            self.protocol("=", 3)
            self.protocol_result(intermediate, 4)

            self.insert_scroll_table()
            result = self.expression.first_number * (1.0 - number / 100.0)
            self.protocol(number, 0)
            self.protocol("% discount of", 1)
            self.protocol(self.expression.first_number, 2)
            self.protocol("=", 3)
            self.protocol_result(result, 4)
        else:
            QMessageBox.information(None, "Information", "Operation not supported for this type of expression.")

        return result