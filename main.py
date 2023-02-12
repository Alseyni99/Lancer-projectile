import interface
import sys 
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    win = interface.quadratic()
    win.show()
    sys.exit(app.exec_())

def f():
    return 0
    
if __name__ == '__main__':
    main()