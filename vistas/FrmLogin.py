
from PyQt5 import QtCore, QtGui, QtWidgets
from recursos import LogoHR_rc
from vistas.FrmPrincipal import Ui_FrmPrincipal
#from controlador.CtrlFrmLogin import CtrlFrmLogin

class Ui_FrmLogin(object):
    def setupUi(self, FrmLogin):
        FrmLogin.setObjectName("FrmLogin")
        FrmLogin.resize(380, 345)
        FrmLogin.setMaximumSize(QtCore.QSize(380, 345))
        icon = QtGui.QIcon.fromTheme("HR")
        FrmLogin.setWindowIcon(icon)
        #self.centrar()
        self.centralwidget = QtWidgets.QWidget(FrmLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.le_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.le_usuario.setGeometry(QtCore.QRect(30, 170, 321, 25))
        self.le_usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.le_usuario.setObjectName("le_usuario")
        self.le_contrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.le_contrasena.setGeometry(QtCore.QRect(30, 220, 321, 25))
        self.le_contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_contrasena.setAlignment(QtCore.Qt.AlignCenter)
        self.le_contrasena.setObjectName("le_contrasena")
        self.btn_entrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_entrar.setGeometry(QtCore.QRect(30, 270, 321, 25))
        self.btn_entrar.setStyleSheet("background-color: rgb(87, 227, 137);")
        self.btn_entrar.setObjectName("btn_entrar")
        self.lbl_logo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logo.setGeometry(QtCore.QRect(130, 20, 131, 131))
        self.lbl_logo.setObjectName("lbl_logo")

        #Eventos
        #self.btn_entrar.clicked.connect(self.btnEntrarClicked)


        FrmLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmLogin)
        QtCore.QMetaObject.connectSlotsByName(FrmLogin)

    def retranslateUi(self, FrmLogin):
        _translate = QtCore.QCoreApplication.translate
        FrmLogin.setWindowTitle(_translate("FrmLogin", "Inicio de sesión"))
        self.le_usuario.setPlaceholderText(_translate("FrmLogin", "Nombre de usuario"))
        self.le_contrasena.setPlaceholderText(_translate("FrmLogin", "Contraseña"))
        self.btn_entrar.setText(_translate("FrmLogin", "Entrar"))
        self.lbl_logo.setText(_translate("FrmLogin", "<html><head/><body><p><img src=\":/newPrefix/HrLogo128.png\"/></p></body></html>"))

    def centrar(self):
        #obtener el tamaño de la pantalla principal
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry()

        # Obtener el tamaño  de la ventana de inicio de sesión
        login_geometry = FrmLogin.geometry()

        # Centrar la ventana de inicio de sesión en la pantalla principal
        x = (screen_geometry.width() - login_geometry.width()) //2
        y = (screen_geometry.height() - login_geometry.height()) //2
        FrmLogin.move(x, y)

    #def btnEntrarClicked(self):
        #self.frm_login = CtrlFrmLogin()
        #self.frm_login.validarCredenciales()
        #self.frm_principal = QtWidgets.QMainWindow()
        #self.uiA = Ui_FrmPrincipal()
        #self.uiA.setupUi(self.frm_principal)
        #self.frm_principal.show()
        #FrmLogin.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmLogin = QtWidgets.QMainWindow()
    ui = Ui_FrmLogin()
    ui.setupUi(FrmLogin)
    FrmLogin.show()
    sys.exit(app.exec_())
