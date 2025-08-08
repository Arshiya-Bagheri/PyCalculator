"""
run.py

Entry point for the calculator application using PySide6.

This script initializes the QApplication, creates the main calculator window,
and starts the Qt event loop.
"""

import sys
from PySide6.QtWidgets import QApplication
from calculator_back import Calculator

# Create the Qt application
app = QApplication(sys.argv)

# Create and show the main calculator window
window = Calculator()
window.show()

# Start the Qt event loop
app.exec()