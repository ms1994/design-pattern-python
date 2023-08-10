"""
    El template method tienes una estructura para ejecutar un proceso, en este ejemplo una orden para comprar o vender btc
    esa estructura tiene metodos que pueden cambiar, entonces haces una interface con todos los metodos de la estructuras
    y los que varian seran abstract methods que seran implementados por diferentes concrete class.

    La interface tendra abstract methods y los methods principales que no quieres que sean overwriting por las subclases,
    el template disena todos los methods y las subclases modificara los abstract methods (tambien puede variar elementos)

    El metodo en el abstract class llamara al metodo abstract y este metodo abstract lo implementara los hijos, siempre
    y cuando llames a la subclass, y ejecutes el metodo, estos abstract methods estaran definidos, independientemente que
    en el template interface no lo esten.

    El template design pattern existira un template method que ejecutara todos (o casi todos) tus metodos en la
    interface no importa que esos metodos no esten definidos(abstract methods), porque luego sera sobreescrito por
    las subclass que cuando implementen el template method (en el ejemplo es el check_prices function), estaran
    implementados. 
"""
from concrete_class import AverageStrategy, MinMaxStrategy
if __name__ == '__main__':
    # Call the strategy that you want.
    strategy = MinMaxStrategy()
    strategy.check_prices("BTC")

    strategy2 = AverageStrategy()
    strategy2.check_prices("EUR")

