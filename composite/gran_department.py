from interface import IDepartment

class GranDepartment(IDepartment):
    """Child class que no sera una hoja sino que tiene varios department de tipo Idepartment"""

    def __init__(self, empleados):
        self.empleados = empleados
        self.empleados_originales = empleados
        self.sub_departamentos = []

    def agregar_departamentos(self, department):
        """
            Clase para agregar department al gran department class
            
            :Params department: Departamentos a agregar
            :TYpe department: Class IDepartment
        """
        self.sub_departamentos.append(department)
        self.empleados += department.empleados

    def print_departamentos(self):
        for department in self.sub_departamentos:
            department.print_departamentos()
        print("El gran department tiene ", self.empleados_originales, " empleados")
        print("La empresa (o IDepartment class) tiene en total ", self.empleados)
