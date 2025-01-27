from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from inst import txt_hello, txt_instruction, txt_next
from test import *

class MainWin(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()
    self.connects()
    self.show()
  def initUI(self):
    self.btn_next = QPushButton(txt_next, self)
    self.hello_text = QLabel(txt_hello)
    self.instruction = QLabel(txt_instruction)

    self.setWindowTitle("Тест Томаса-Килмана")
    self.layout_line = QVBoxLayout()
    self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
    self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
    self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
    self.setLayout(self.layout_line)
  def connects(self):
    self.btn_next.clicked.connect(self.next_click)
  def next_click(self):
    self.hide()
    self.tw = TestWin()





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWin = MainWin()
    sys.exit(app.exec_())