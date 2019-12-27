#!/usr/bin/env python3

# Filename: pycalc.py

'''PyCalc is a simple calculator built using Python and PyQt5.'''

from functools import partial
import sys

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


__version__ = '0.1'
__author__ = 'Daniel'

# Create a subclass of QMainWindow to setup the calculator's GUI
class PyCalcUi(QMainWindow):
  """PyCalc's View (GUI)."""
  def __init__(self):
    """View initializer."""
    super().__init__()
    # Set some main window's properties
    self.setWindowTitle('PyCalc')
    self.setFixedSize(235, 235)
    # Set the central widget and general layout
    self.generalLayout = QVBoxLayout()
    self._centralWidget = QWidget(self)
    self.setCentralWidget(self._centralWidget)
    self._centralWidget.setLayout(self.generalLayout)
    # Create the display and the buttons
    self._createDisplay()
    self._createButtons()

  def _createDisplay(self):
    """Create the display."""
    # Create the display widget
    self.display = QLineEdit()
    # Set some display's properties
    self.display.setFixedHeight(35)
    self.display.setAlignment(Qt.AlignRight)
    self.display.setReadOnly(True)
    # Add the display to the general layout
    self.generalLayout.addWidget(self.display)

  def _createButtons(self):
    """Create the buttons."""
    self.buttons = {}
    buttonsLayout = QGridLayout()
    # Button text | position on the QGridLayout
    rows = ['789/C', 
            '456*(', 
	    '123-)', 
	    ('0', '00', '.', '+', '=')]
    buttons = {v: (i, j) for i, line in enumerate(rows) for j, v in enumerate(line)}

    for btnText, pos in buttons.items():
      self.buttons[btnText] = QPushButton(btnText)
      self.buttons[btnText].setFixedSize(40, 40)
      buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])

    # Add buttonsLayout to the general layout
    self.generalLayout.addLayout(buttonsLayout)

  def setDisplayText(self, text):
    """Set display's text."""
    self.display.setText(text)
    self.display.setFocus()

  def displayText(self):
    """Get display's text."""
    return self.display.text()

  def clearDisplay(self):
    """Clear the display."""
    self.setDisplayText('')

class PyCalcCtrl:
  """PyCalc Controller class."""
  def __init__(self, view):
    """Controller initializer."""
    self._view = view
    # Connect signals and slots
    self._connectSignals()

  def _buildExpression(self, sub_exp):
    """Build expression."""
    expression = self._view.displayText() + sub_exp
    self._view.setDisplayText(expression)

  def _connectSignals(self):
    """Connect signals and slots."""
    for btnText, btn in self._view.buttons.items():
      if btnText not in {'=', 'C'}:
        btn.clicked.connect(partial(self._buildExpression, btnText))
 
    self._view.buttons['C'].clicked.connect(self._view.clearDisplay)

# Client code
def main():
  """Main function."""
  # Create an instance of QApplication
  app = QApplication(sys.argv)
  # Show the calculator's GUI
  view = PyCalcUi()
  controller = PyCalcCtrl(view)
  view.show()
  # Execute the calculator's main loop
  sys.exit(app.exec())

if __name__ == '__main__':
  main()
