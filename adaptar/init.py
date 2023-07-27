"""
    El adapter design pattern utiliza el interface de la clase A para ejecutar los metodos de una clase B.
    Creando una instancia del objeto B, en el adapter class
"""
from classA import A
from classB import B
from classBAdapter import BAdapter

if __name__ == '__main__':

    # Metodo A
    item = A()
    item.method_a()

    # Si el item es de clase b, no podremos utilizar el metodo A
    try:
        item = B()
        item.method_a()
    except:
        print('No se pudo ejecutar ese metodo')

    # Usamos el adapter para utilizar el metodo A, con el objeto B

    item = B()

    item_adapter = BAdapter(item)

    item_adapter.method_a()

