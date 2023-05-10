
from PyQt5 import QtCore, QtGui, QtWidgets
from recursos import LogoPrincipal_rc
from vistas.FrmAsignarFunciones import Ui_FrmAsignarFunciones
from vistas.FrmAsignarRoles import Ui_FrmAsignarRoles
from vistas.FrmDepartamentos import Ui_FrmDepartamentos
from vistas.FrmDependiente import Ui_FrmDependiente
from vistas.FrmEmpleado import Ui_FrmEmpleado
from vistas.FrmLocalizacion import Ui_FrmLocalizacion
from vistas.FrmPais import Ui_FrmPais
from vistas.FrmRegion import Ui_FrmRegion
from vistas.FrmRol import Ui_FrmRol
from vistas.FrmTrabajo import Ui_FrmTrabajo


class Ui_FrmPrincipal(object):
    def setupUi(self, FrmPrincipal):
        FrmPrincipal.setObjectName("FrmPrincipal")
        FrmPrincipal.resize(1303, 906)
        self.centralwidget = QtWidgets.QWidget(FrmPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_logo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logo.setGeometry(QtCore.QRect(330, 197, 642, 512))
        self.lbl_logo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_logo.setObjectName("lbl_logo")
        FrmPrincipal.setCentralWidget(self.centralwidget)
        #self.centrar()
        self.menubar = QtWidgets.QMenuBar(FrmPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1303, 22))
        self.menubar.setObjectName("menubar")
        self.menuEmpleados = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuEmpleados.setFont(font)
        self.menuEmpleados.setObjectName("menuEmpleados")
        self.menuSeguridad = QtWidgets.QMenu(self.menubar)
        self.menuSeguridad.setObjectName("menuSeguridad")
        FrmPrincipal.setMenuBar(self.menubar)
        self.btn_gestionTrabajos = QtWidgets.QAction(FrmPrincipal)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_gestionTrabajos.setFont(font)
        self.btn_gestionTrabajos.setObjectName("btn_gestionTrabajos")
        self.Btn_gestionEmpleados = QtWidgets.QAction(FrmPrincipal)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Btn_gestionEmpleados.setFont(font)
        self.Btn_gestionEmpleados.setObjectName("Btn_gestionEmpleados")
        self.btn_gestionDepartamentos = QtWidgets.QAction(FrmPrincipal)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_gestionDepartamentos.setFont(font)
        self.btn_gestionDepartamentos.setObjectName("btn_gestionDepartamentos")
        self.btn_gestionLocalizacion = QtWidgets.QAction(FrmPrincipal)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_gestionLocalizacion.setFont(font)
        self.btn_gestionLocalizacion.setObjectName("btn_gestionLocalizacion")
        self.btn_gestionPais = QtWidgets.QAction(FrmPrincipal)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_gestionPais.setFont(font)
        self.btn_gestionPais.setObjectName("btn_gestionPais")
        self.btn_gestionRegion = QtWidgets.QAction(FrmPrincipal)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_gestionRegion.setFont(font)
        self.btn_gestionRegion.setObjectName("btn_gestionRegion")
        self.btn_gestionDependientes = QtWidgets.QAction(FrmPrincipal)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_gestionDependientes.setFont(font)
        self.btn_gestionDependientes.setObjectName("btn_gestionDependientes")
        self.btn_gestionUsuario = QtWidgets.QAction(FrmPrincipal)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_gestionUsuario.setFont(font)
        self.btn_gestionUsuario.setObjectName("btn_gestionUsuario")
        self.btn_gestionRol = QtWidgets.QAction(FrmPrincipal)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_gestionRol.setFont(font)
        self.btn_gestionRol.setObjectName("btn_gestionRol")
        self.btn_asignarRol = QtWidgets.QAction(FrmPrincipal)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_asignarRol.setFont(font)
        self.btn_asignarRol.setObjectName("btn_asignarRol")
        self.btn_asignarFuncionesRol = QtWidgets.QAction(FrmPrincipal)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_asignarFuncionesRol.setFont(font)
        self.btn_asignarFuncionesRol.setObjectName("btn_asignarFuncionesRol")
        self.menuEmpleados.addAction(self.btn_gestionTrabajos)
        self.menuEmpleados.addAction(self.Btn_gestionEmpleados)
        self.menuEmpleados.addAction(self.btn_gestionDependientes)
        self.menuEmpleados.addAction(self.btn_gestionDepartamentos)
        self.menuEmpleados.addAction(self.btn_gestionLocalizacion)
        self.menuEmpleados.addAction(self.btn_gestionPais)
        self.menuEmpleados.addAction(self.btn_gestionRegion)
        self.menuSeguridad.addAction(self.btn_gestionUsuario)
        self.menuSeguridad.addAction(self.btn_gestionRol)
        self.menuSeguridad.addAction(self.btn_asignarRol)
        self.menuSeguridad.addAction(self.btn_asignarFuncionesRol)
        self.menubar.addAction(self.menuEmpleados.menuAction())
        self.menubar.addAction(self.menuSeguridad.menuAction())

        #Eventos
        self.btn_gestionTrabajos.triggered.connect(self.btn_gestionTrabajo_triggered)
        self.btn_gestionPais.triggered.connect(self.btn_gestionPais_triggered)
        self.btn_gestionRegion.triggered.connect(self.btn_gestionRegion_triggered)
        self.btn_gestionRol.triggered.connect(self.btn_gestionRol_triggered)
        self.btn_gestionUsuario.triggered.connect(self.btn_gestionUsuario_triggered)
        self.btn_gestionDepartamentos.triggered.connect(self.btn_gestionDepartamentos_triggered)
        self.btn_gestionDependientes.triggered.connect(self.btn_gestionDependientes_triggered)
        self.btn_gestionLocalizacion.triggered.connect(self.btn_gestionLocalizacion_triggered)
        self.btn_asignarRol.triggered.connect(self.btn_asignarRol_triggered)
        self.btn_asignarFuncionesRol.triggered.connect(self.btn_asignarFuncionesRol_triggered)
        self.Btn_gestionEmpleados.triggered.connect(self.btn_gestionEmpleados_triggered)






        self.retranslateUi(FrmPrincipal)
        QtCore.QMetaObject.connectSlotsByName(FrmPrincipal)

    def btn_gestionTrabajo_triggered(self):
        self.FrmTrabajo = QtWidgets.QMainWindow()  # Se cambia a QMainWindow
        self.ui_trabajo = Ui_FrmTrabajo()  # ui_trabajo se hace un atributo de la clase
        self.ui_trabajo.setupUi(self.FrmTrabajo)
        self.FrmTrabajo.show()

    def btn_gestionEmpleados_triggered(self):
        self.FrmEmpleado = QtWidgets.QMainWindow()  # Se cambia a QMainWindow
        self.ui_empleado = Ui_FrmEmpleado()  # ui_trabajo se hace un atributo de la clase
        self.ui_empleado.setupUi(self.FrmEmpleado)
        self.FrmEmpleado.show()

    def btn_asignarFuncionesRol_triggered(self):
        self.FrmAsignarFunciones = QtWidgets.QMainWindow()  # Se cambia a QMainWindow
        self.ui_funciones = Ui_FrmAsignarFunciones()  # ui_trabajo se hace un atributo de la clase
        self.ui_funciones.setupUi(self.FrmAsignarFunciones)
        self.FrmAsignarFunciones.show()

    def btn_asignarRol_triggered(self):
        self.FrmAsignarRoles = QtWidgets.QMainWindow()  # Se cambia a QMainWindow
        self.ui_roles = Ui_FrmAsignarRoles()  # ui_trabajo se hace un atributo de la clase
        self.ui_roles.setupUi(self.FrmAsignarRoles)
        self.FrmAsignarRoles.show()

    def btn_gestionPais_triggered(self):
        self.FrmPais = QtWidgets.QMainWindow()  # Se cambia a QMainWindow
        self.ui_pais = Ui_FrmPais()  # ui_trabajo se hace un atributo de la clase
        self.ui_pais.setupUi(self.FrmPais)
        self.FrmPais.show()

    def btn_gestionRegion_triggered(self):
        self.FrmRegion = QtWidgets.QMainWindow()  # Se cambia a QMainWindow
        self.ui_region = Ui_FrmRegion()  # ui_trabajo se hace un atributo de la clase
        self.ui_region.setupUi(self.FrmRegion)
        self.FrmRegion.show()

    def btn_gestionRol_triggered(self):
        self.FrmRol = QtWidgets.QMainWindow()  # Se cambia a QMainWindow
        self.ui_rol = Ui_FrmRol()  # ui_trabajo se hace un atributo de la clase
        self.ui_rol.setupUi(self.FrmRol)
        self.FrmRol.show()

    def btn_gestionUsuario_triggered(self):
        self.FrmUsuarios = QtWidgets.QMainWindow()  # Se cambia a QMainWindow
        self.ui_usuarios = Ui_FrmEmpleado()  # ui_trabajo se hace un atributo de la clase
        self.ui_usuarios.setupUi(self.FrmUsuarios)
        self.FrmUsuarios.show()

    def btn_gestionDepartamentos_triggered(self):
        self.FrmDepartamentos = QtWidgets.QMainWindow()  # Se cambia a QMainWindow
        self.ui_departamentos = Ui_FrmDepartamentos()  # ui_trabajo se hace un atributo de la clase
        self.ui_departamentos.setupUi(self.FrmDepartamentos)
        self.FrmDepartamentos.show()

    def btn_gestionDependientes_triggered(self):
        self.FrmDependiente = QtWidgets.QMainWindow()  # Se cambia a QMainWindow
        self.ui_dependiente = Ui_FrmDependiente()  # ui_trabajo se hace un atributo de la clase
        self.ui_dependiente.setupUi(self.FrmDependiente)
        self.FrmDependiente.show()


    def btn_gestionLocalizacion_triggered(self):
        self.FrmLocalizacion = QtWidgets.QMainWindow()  # Se cambia a QMainWindow
        self.ui_localizacion = Ui_FrmLocalizacion()  # ui_trabajo se hace un atributo de la clase
        self.ui_localizacion.setupUi(self.FrmLocalizacion)
        self.FrmLocalizacion.show()


    def retranslateUi(self, FrmPrincipal):
        _translate = QtCore.QCoreApplication.translate
        FrmPrincipal.setWindowTitle(_translate("FrmPrincipal", "Principal"))
        self.lbl_logo.setText(_translate("FrmPrincipal", "<html><head/><body><p><img src=\":/newPrefix/HR512.png\"/></p></body></html>"))
        self.menuEmpleados.setTitle(_translate("FrmPrincipal", "Recursos Humanos"))
        self.menuSeguridad.setTitle(_translate("FrmPrincipal", "Seguridad"))
        self.btn_gestionTrabajos.setText(_translate("FrmPrincipal", "Gestión Trabajos"))
        self.Btn_gestionEmpleados.setText(_translate("FrmPrincipal", "Gestión Empleados"))
        self.btn_gestionDepartamentos.setText(_translate("FrmPrincipal", "Gestión Departamentos"))
        self.btn_gestionLocalizacion.setText(_translate("FrmPrincipal", "Gestión Localización "))
        self.btn_gestionPais.setText(_translate("FrmPrincipal", "Gestión Pais"))
        self.btn_gestionRegion.setText(_translate("FrmPrincipal", "Gestión región"))
        self.btn_gestionDependientes.setText(_translate("FrmPrincipal", "Gestión Dependientes"))
        self.btn_gestionUsuario.setText(_translate("FrmPrincipal", "Gestión Usuario"))
        self.btn_gestionRol.setText(_translate("FrmPrincipal", "Gestión Rol"))
        self.btn_asignarRol.setText(_translate("FrmPrincipal", "Asignar Rol"))
        self.btn_asignarFuncionesRol.setText(_translate("FrmPrincipal", "Asignar Funciones al rol"))

    def centrar(self):
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry()

        # Obtener el tamaño  de la ventana de inicio de sesión
        login_geometry = FrmPrincipal.geometry()

        # Centrar la ventana de inicio de sesión en la pantalla principal
        x = (screen_geometry.width() - login_geometry.width()) // 2
        y = (screen_geometry.height() - login_geometry.height()) // 2
        FrmPrincipal.move(x, y)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmPrincipal = QtWidgets.QMainWindow()
    ui = Ui_FrmPrincipal()
    ui.setupUi(FrmPrincipal)
    FrmPrincipal.show()
    sys.exit(app.exec_())
