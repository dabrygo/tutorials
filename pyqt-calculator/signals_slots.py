# Filename: signals_slots.py

'''Signals and slots example.'''

import functools
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

def greeting():
  """Slot function."""
  if msg.text():
    msg.setText("")
  else:
    msg.setText("Hello World!")

def greet2(who):
  """Slot function."""
  if msg.text():
    msg.setText("")
  else:
    msg.setText(f"Hello {who}!")



app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
#btn.clicked.connect(greeting) # Connect clicked to greeting()
#btn.clicked.connect(functools.partial(greet2, "World"))
btn.clicked.connect(lambda x: greet2("World"))



layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
