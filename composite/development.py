from interface import IDepartment

class DevelopmentDepartment(IDepartment):
    """Child del IDepartment class"""

    def __init__(self, empleados):
        """Ejecuta su propio metodo sobreescribiendo el del parent class"""
        self.empleados = empleados

    def print_departamentos(self):
        print("Development department tiene ",self.empleados, " empleados")