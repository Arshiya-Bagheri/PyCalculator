"""
calculator_back.py

A simple calculator backend using PySide6 for GUI and Python's AST module for safe expression evaluation.

This module defines:
- safe_eval: A function to safely evaluate mathematical expressions.
- Calculator: The main window class for the calculator GUI.
"""

import ast
import operator
from PySide6.QtWidgets import QMainWindow
from ui_calculator import Ui_Calculator

def safe_eval(expr):
    """
    Safely evaluates a mathematical expression using Python's AST module.

    Supported operators:
        +, -, *, /, unary -

    Args:
        expr (str): The mathematical expression to evaluate.

    Returns:
        float|int: The result of the evaluated expression.

    Raises:
        ValueError: If the expression contains unsupported operations.
    """
    ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg
    }

    def _eval(node):
        if isinstance(node, ast.Num):  # <number>
            return node.n
        elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
            return ops[type(node.op)](_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp):  # - <operand>
            return ops[type(node.op)](_eval(node.operand))
        else:
            raise ValueError("Unsupported expression")

    return _eval(ast.parse(expr, mode='eval').body)

class Calculator(QMainWindow):
    """
    Main calculator window class.

    Handles UI setup, button connections, and calculator logic.
    """

    def __init__(self):
        """
        Initializes the calculator window, sets up the UI, and connects buttons to their respective methods.
        """
        super().__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        self.setWindowTitle('Calculator')

        # Connect digit buttons using a loop
        for i in range(10):
            getattr(self.ui, f'button_{i}').clicked.connect(lambda _, x=str(i): self.append_text(x))

        # Connect operator buttons
        self.ui.point.clicked.connect(lambda: self.append_text("."))
        self.ui.sum.clicked.connect(lambda: self.append_text("+"))
        self.ui.sub.clicked.connect(lambda: self.append_text("-"))
        self.ui.multiple.clicked.connect(lambda: self.append_text("*"))
        self.ui.division.clicked.connect(lambda: self.append_text("/"))

        # Connect other buttons
        self.ui.equal.clicked.connect(self.method_equal)
        self.ui.clear.clicked.connect(self.method_clear)
        self.ui.delete_2.clicked.connect(self.method_del)

    def append_text(self, value):
        """
        Appends a value (digit or operator) to the calculator display.

        If the display shows an error message, it clears it before appending.

        Args:
            value (str): The value to append.
        """
        text = self.ui.label.text()
        if text == "Wrong Input":
            text = ""
        self.ui.label.setText(text + value)

    def method_clear(self):
        """
        Clears the calculator display.
        """
        self.ui.label.setText("")

    def method_del(self):
        """
        Deletes the last character from the calculator display.
        """
        text = self.ui.label.text()
        self.ui.label.setText(text[:-1])

    def method_equal(self):
        """
        Evaluates the expression shown on the calculator display.

        If the expression is invalid, displays an error message.
        """
        text = self.ui.label.text()
        try:
            ans = safe_eval(text)
            self.ui.label.setText(str(ans))
        except Exception:
            self.ui.label.setText("Wrong Input")