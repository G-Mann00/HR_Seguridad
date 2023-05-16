import sys
from PyQt5 import QtWidgets, QtCore
from controlador.CtrlFrmLogin import CtrlFrmLogin

def print_hi(name):
    print(f'Hi, {name}')
    print("Hola Mundo")


if __name__ == '__main__':
    #print_hi('PyCharm')
    app = QtWidgets.QApplication(sys.argv)
    frm = CtrlFrmLogin()
    frm.show()
    sys.exit(app.exec_())


