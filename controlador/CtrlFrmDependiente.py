from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
from vistas.FrmDependiente import Ui_FrmDependiente
from datos.Dt_Dependents import Dt_Dependents
from entidades.Dependents import Dependents


class CtrlFrmDependiente(QtWidgets.QMainWindow):
    dDependent = Dt_Dependents()

    def __init__(self):
        self.listaDependiente = []
        super().__init__()
        self.ui = Ui_FrmDependiente()
        self.ui.setupUi(self)
        # self.initControlGui()
        self.cargarDatosTabla()

    # def initControlGui(self):
        # self.ui.btn_agregar.clicked.connect(self.btnAgregar)

    def cargarDatosTabla(self):
        listaDependientes = self.dDependent.listarDependientes()
        try:
            if listaDependientes == None:
                alert = QMessageBox.information(self, 'Alerta', "No hay ningún dependiente", QMessageBox.Ok)
                return

            self.ui.tw_registrosDependiente.setRowCount(len(listaDependientes))
            self.ui.tw_registrosDependiente.setColumnCount(5)
            # self.ui.tw_registrosDependiente.verticalHeader().setVisible(False)
            row = 0

            for r in listaDependientes:
                self.ui.tw_registrosDependiente.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.dependent_id)))
                self.ui.tw_registrosDependiente.setItem(row, 1, QtWidgets.QTableWidgetItem(r.first_name))
                self.ui.tw_registrosDependiente.setItem(row, 2, QtWidgets.QTableWidgetItem(r.last_name))
                self.ui.tw_registrosDependiente.setItem(row, 3, QtWidgets.QTableWidgetItem(r.relationship))
                self.ui.tw_registrosDependiente.setItem(row, 4, QtWidgets.QTableWidgetItem(r.employee_name))
                row += 1

        except Exception as e:
            print(e)
