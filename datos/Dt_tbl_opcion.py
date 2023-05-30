from datos.conexion import Conexion
from entidades.Tbl_opcion import Tbl_opcion

class Dt_tbl_opcion:
    def __init__(self):
        pass
    _dbCon = Conexion()
    _con = None
    _cursor = None
    _sql = ""

    def llenarCbxOpcion(self):
        self._sql = "SELECT id_opcion, opcion FROM Seguridad.tbl_opcion WHERE estado<>3;"
        try:
            # abrimos la conexion & cursor
            self._con = self._dbCon.getConnection()
            self._cursor = self._dbCon.getCursor()
            # ejecutamos la consulta
            self._cursor.execute(self._sql)
            # Obtenemos todos los registros de la consulta
            registros = self._cursor.fetchall()
            print("Numero total de registros: ", self._cursor.rowcount)
            listaOpcion = []

            for to in registros:
                to = Tbl_opcion(to['id_opcion'], to['opcion'])
                listaOpcion.append(to)
            print('listaOpcion', listaOpcion)
            return listaOpcion

        except Exception as e:
            print("Datos: Error listOpcion()", e)
        finally:
            #self._dbCon.closeCon()
            pass