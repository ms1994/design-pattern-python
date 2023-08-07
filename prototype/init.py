"""
    El prototype pattern sirve para crear una copia shallow o deep de una clase,o instanc
    en vez de tener que referenciarla nuevamente

"""

from concrete_prototype_1 import ShallowPrototype
from concrete_prototype_2 import DeepPrototype

if __name__ == '__main__':

    obj1 =  ShallowPrototype(integer = 25, string="Miquel", list=[ [1,3,4], 2, "34"], dict={1:3, "a":2})

    print(obj1)

    obj_copy = obj1.clone()

    print(obj_copy)

    # Los objetos tienen distinta direccion de memoria probar corriendo el init.py
    obj1.string = "Carmen"
    print(obj1)
    # Los cambios en el original no afectan la primera capa de la copia

    obj_copy.string = "Otra"

    print(obj_copy)

    # AL cambiar la copia shallow de la lista compuesta afecta el original
    obj_copy.list[0][0] = 24

    print("Afecta" , obj1)
    print("copia", obj_copy)

    # Creamos una deep copia para evitar eso
    obj2 = DeepPrototype(integer = 25, string="Miquel", list=[ [1,3,4], 2, "34"], dict={1:3, "a":2})

    obj_copy2 = obj2.clone()

    # No afecta el deep copy
    obj_copy2.list[0][0] = 24
    print("Original deep", obj2)

    print("copia cambiada", obj_copy2)