from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
from vistas.FrmPais import Ui_FrmPais
from datos.Dt_Country import Dt_Country
from datos.Dt_Region import Dt_Region
from entidades.Country import Country


class CtrlFrmPais(QtWidgets.QMainWindow):

    def __init__(self):
        self.listaRegion = [] #nos va permitar para guardar la lista de regiones(incluido su id) y poder usarlo en guardar, editar.
        super().__init__()
        self.ui = Ui_FrmPais()
        self.ui.setupUi(self)
        self.initControlGui()
        self.cargarDatosTabla()
        self.cargarDatosCombobox()


    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.btnAgregar)
        self.ui.tw_registroPais.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.btn_limpiar.clicked.connect(self.limpiarDatos)
        self.ui.tw_registroPais.clicked.connect(self.filaSeleccionada)
        QApplication.instance().focusChanged.connect(self.validarIdentificador)
        self.ui.btn_editar.clicked.connect(self.btnEditar)
        self.ui.btn_eliminar.clicked.connect(self.btnEliminar)
        self.ui.btn_buscar.clicked.connect(self.btnBuscar)
        self.ui.le_buscar.textChanged.connect(self.refresh)

        pass

    def refresh(self):
        if self.ui.le_buscar.text() == "":
            self.cargarDatosTabla()

    def validarIdentificador(self,old_widget, now_widget):

        if self.ui.le_identificador is old_widget:

            #si esta vacio no hacemos nada
            if self.ui.le_identificador.text() == "":
                return

            if len(self.ui.le_identificador.text()) > 2:
                QMessageBox.warning(self, "Error", "El identificador no puede tener más de 2 caracteres")
                #self.ui.le_identificador.setFocus()
                return


    def filaSeleccionada(self):
        if len(self.ui.tw_registroPais.selectedItems()) > 0:
            row = self.ui.tw_registroPais.selectedItems()[0].row()
            self.ui.le_identificador.setText(self.ui.tw_registroPais.item(row, 0).text())
            self.ui.le_nombre.setText(self.ui.tw_registroPais.item(row, 1).text())
            self.ui.cmb_region.setCurrentText(self.ui.tw_registroPais.item(row, 2).text())
        self.ui.le_identificador.setEnabled(False)
    def cargarDatosCombobox(self):
        dRegion = Dt_Region()
        self.listaRegion = dRegion.listarRegion()

        self.ui.cmb_region.clear()
        self.ui.cmb_region.addItem("---Seleccione---")
        for r in self.listaRegion:
            self.ui.cmb_region.addItem(r.region_name)


    def cargarDatosTabla(self):
        dCountry = Dt_Country()
        listaPaises = dCountry.listarPaises()

        if listaPaises == None:
            alert = QMessageBox.information(self, 'Alerta', "No hay ningún país", QMessageBox.Ok)
            return

        self.ui.tw_registroPais.setRowCount(len(listaPaises))
        self.ui.tw_registroPais.setColumnCount(3)
        self.ui.tw_registroPais.verticalHeader().setVisible(False)
        row = 0
        for r in listaPaises:
            self.ui.tw_registroPais.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.country_id)))
            self.ui.tw_registroPais.setItem(row, 1, QtWidgets.QTableWidgetItem(r.country_name))
            self.ui.tw_registroPais.setItem(row, 2, QtWidgets.QTableWidgetItem(str(r.region_id)))
            row += 1

    def limpiarDatos(self):
        self.ui.le_identificador.setText("")
        self.ui.le_nombre.setText("")
        self.ui.cmb_region.setCurrentIndex(0)
        self.ui.le_identificador.setEnabled(True)

    def btnAgregar(self):
        if self.ui.le_nombre.text() == "" or self.ui.cmb_region.currentIndex() == 0 or self.ui.le_identificador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return



        dCountry = Dt_Country()
        c = Country()
        c.country_id = self.ui.le_identificador.text()
        c.country_name = self.ui.le_nombre.text()
        index = self.ui.cmb_region.currentText()
        c.region_id = self.obtenerRegionId(index)

        if dCountry.validarIdUnico(self.ui.le_identificador.text()):
            QMessageBox.warning(self, "Error", "Existe un registro con el mismo identificador")
            return

        if not dCountry.insertarPais(c):
            QMessageBox.warning(self, "Error", "No se pudo guardar el registro")
            return
        QMessageBox.information(self, "Éxito", "Se guardó el registro")
        self.cargarDatosTabla()
        self.limpiarDatos()

    def obtenerRegionId(self, region_name):
        for r in self.listaRegion:
            if r.region_name == region_name:
                return r.region_id
        return -1

    def btnEditar(self):
        if self.ui.le_nombre.text() == "" or self.ui.cmb_region.currentIndex() == 0 or self.ui.le_identificador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return

        if len(self.ui.le_identificador.text()) > 2:
            QMessageBox.warning(self, "Error", "El identificador no puede tener más de 2 caracteres")
            return

        dCountry = Dt_Country()
        c = Country()
        c.country_id = self.ui.le_identificador.text()
        c.country_name = self.ui.le_nombre.text()
        index = self.ui.cmb_region.currentText()
        c.region_id = self.obtenerRegionId(index)



        if not dCountry.actualizarPais(c):
            QMessageBox.warning(self, "Error", "No se pudo editar el registro")
            return
        QMessageBox.information(self, "Éxito", "Se editó el registro")
        self.cargarDatosTabla()
        self.limpiarDatos()

    def btnEliminar(self):
        if self.ui.le_identificador.text() == "":
            return

        if len(self.ui.le_identificador.text()) > 2:
            QMessageBox.warning(self, "Error", "El identificador no puede tener más de 2 caracteres")
            return

        dCountry = Dt_Country()
        c = Country()
        c.country_id = self.ui.le_identificador.text()
        c.country_name = self.ui.le_nombre.text()


        alert = QMessageBox.warning(self, 'Alerta', f"¿Está seguro de eliminar el pais {c.country_name}?", QMessageBox.Yes | QMessageBox.No)
        if alert == QMessageBox.No:
            return

        if not dCountry.eliminarPais(c):
            QMessageBox.warning(self, "Error", "No se pudo eliminar el registro")
            return
        QMessageBox.information(self, "Éxito", "Se eliminó el registro")
        self.cargarDatosTabla()
        self.limpiarDatos()

    def btnBuscar(self):
        if self.ui.le_buscar.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese el nombre del país")
            return

        dCountry = Dt_Country()
        c = Country()
        c.country_name = self.ui.le_buscar.text()
        listaPaises = dCountry.buscarPais(c)

        if listaPaises == None:
            alert = QMessageBox.information(self, 'Alerta', "No hay ningún país", QMessageBox.Ok)
            return

        self.ui.tw_registroPais.setRowCount(len(listaPaises))
        self.ui.tw_registroPais.setColumnCount(3)
        self.ui.tw_registroPais.verticalHeader().setVisible(False)
        row = 0
        for r in listaPaises:
            self.ui.tw_registroPais.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.country_id)))
            self.ui.tw_registroPais.setItem(row, 1, QtWidgets.QTableWidgetItem(r.country_name))
            self.ui.tw_registroPais.setItem(row, 2, QtWidgets.QTableWidgetItem(str(r.region_id)))
            row += 1