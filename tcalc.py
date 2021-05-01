import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

__version__ = '0.0.1'
__author__ = 'Daniel P. Teberian'


class TCalcUI(QMainWindow):
   def __init__(self):
      super().__init__()
      self.setWindowTitle('TCalculator - v0.0.1')
      self.setFixedSize(235, 235)
      self._centralWidget = QWidget(self)
      self.setCentralWidget(self._centralWidget)

def main():
   tcalc = QApplication(sys.argv)
   view = TCalcUI()
   view.show()
   sys.exit(tcalc.exec_())

if __name__ == '__main__':
   main()
