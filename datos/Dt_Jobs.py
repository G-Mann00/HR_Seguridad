from entidades.Jobs import Jobs
from datos.conexion import Conexion


class Dt_Jobs:
    _con = None
    _cursor = None

    def __init__(self):
        pass

    def listarTrabajo(self):
        listaTrabajo = []
        try:

            self._con = Conexion.getConnection()
            self._cursor = Conexion.getCursor()

            sql = "SELECT * FROM Seguridad.jobs;"
            self._cursor.execute(sql)

            registros = self._cursor.fetchall()
            for r in registros:
                id = r['job_id']
                nombre = r['job_title']
                minimo = r['min_salary']
                maximo = r['max_salary']
                trabajo = Jobs(id, nombre, minimo, maximo)
                listaTrabajo.append(trabajo)
            self._cursor.close()
            return listaTrabajo

        except Exception as e:
            print("Datos: Error en listarTrabajo", e)

        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


    def filtrarTrabajo(self, jobs_param):
        listaTrabajo = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = Conexion.getCursor()

            sql = f"SELECT * FROM Seguridad.jobs WHERE job_title like '%{jobs_param.job_title}%';"
            self._cursor.execute(sql)

            registros = self._cursor.fetchall()
            for r in registros:
                id = r['job_id']
                nombre = r['job_title']
                minimo = r['min_salary']
                maximo = r['max_salary']
                trabajo = Jobs(id, nombre, minimo, maximo)
                listaTrabajo.append(trabajo)
            return listaTrabajo

        except Exception as e:
            print("Datos: Error en filtrarTrabajo", e)

        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


    def buscar(self, jobs_param):
        listaTrabajo = []
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            print(con.open)
            if cursor:
                print("Estoy abierto")
            else:
                print("Estoy cerrado")
            sql = f"SELECT * FROM Seguridad.jobs WHERE job_title LIKE '%{jobs_param.job_title}%';"
            num = cursor.execute(sql)
            print(f"Hola soy el resultado del executre : {num}")
            registros = cursor.fetchall()
            for r in registros:
                id = r['job_id']
                nombre = r['job_title']
                minimo = r['min_salary']
                maximo = r['max_salary']
                trabajo = Jobs(id, nombre, minimo, maximo)
                listaTrabajo.append(trabajo)
                print(f"Trabajo: {trabajo}")
            return listaTrabajo

        except Exception as e:
            print("Error en la consulta", e)

        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


    def insertarTrabajo(self, jobs_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = Conexion.getCursor()
            sql = f"INSERT INTO Seguridad.jobs(job_title, min_salary, max_salary) VALUES ('{jobs_param.job_title}', '{jobs_param.min_salary}', '{jobs_param.max_salary}');"
            if self._cursor.execute(sql) > 0:
                resultado = True
            self._con.commit()
            return resultado

        except Exception as e:
            print(f"Datos: Error en insertarTrabajo", e)

        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


    def actualizarTrabajo(self, jobs_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = Conexion.getCursor()
            sql = f"UPDATE Seguridad.jobs SET job_title = '{jobs_param.job_title}', min_salary = '{jobs_param.min_salary}', max_salary = '{jobs_param.max_salary}' WHERE job_id = {jobs_param.job_id};"
            if self._cursor.execute(sql) > 0:
                resultado = True
            self._con.commit()
            return resultado

        except Exception as e:
            print(f"Datos: Error en la actualizarTrabajo", e)

        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def eliminarTrabajo(self, jobs_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = Conexion.getCursor()
            sql = f"DELETE FROM Seguridad.jobs WHERE job_id = {jobs_param.job_id};"
            if self._cursor.execute(sql) > 0:
                resultado = True
            self._con.commit()
            return resultado

        except Exception as e:
            print(f"Datos: Error en eliminarTrabajo", e)

        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def existeTrabajo(self, jobs_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = Conexion.getCursor()

            sql = f"SELECT * FROM Seguridad.jobs WHERE job_title like '%{jobs_param.job_title}%';"
            self._cursor.execute(sql)

            if self._cursor.rowcount > 0:
                resultado = True
            return resultado

        except Exception as e:
            print(f"Datos: Error en existeTrabajo", e)

        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
