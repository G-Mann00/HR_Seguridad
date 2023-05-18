from entidades.Jobs import Jobs
from datos.conexion import Conexion


class Dt_Jobs:

    def __init__(self):
        self._con = None
        self._cursor = None


    def listarTrabajo(self):
        listaTrabajo = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()

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
            print("Error en la consulta", e)
            if self._con.open:
                self._con.close()
                self._cursor.close()
                print("MySQL connection was closed")


    def buscarTrabajo(self, jobs_param):
        listaTrabajo = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()

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
                print(f"Trabajo: {trabajo}")
            self._cursor.close()
            return listaTrabajo
        except Exception as e:
            print("Error en la consulta", e)
            if self._con.open:
                self._con.close()
                self._cursor.close()
                print("MySQL connection was closed")


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
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"INSERT INTO Seguridad.jobs(job_title, min_salary, max_salary) VALUES ('{jobs_param.job_title}', '{jobs_param.min_salary}', '{jobs_param.max_salary}');"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()
        except Exception as e:
            print(f"Error en la insercion: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado


    def actualizarTrabajo(self, jobs_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"UPDATE Seguridad.jobs SET job_title = '{jobs_param.job_title}', min_salary = '{jobs_param.min_salary}', max_salary = '{jobs_param.max_salary}' WHERE job_id = {jobs_param.job_id};"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()
        except Exception as e:
            print(f"Error en la actualizacion: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def eliminarTrabajo(self, jobs_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"DELETE FROM Seguridad.jobs WHERE job_id = {jobs_param.job_id};"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()
        except Exception as e:
            print(f"Error en la eliminacion: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado