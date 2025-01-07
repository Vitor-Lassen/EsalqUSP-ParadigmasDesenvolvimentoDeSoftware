from abc import ABC, abstractmethod


class FormaGeometrica (ABC):
    
    @abstractmethod
    def calcular_area(self):
        raise NotImplementedError("Método abstrato deve ser implementado")
    
    # @abstractmethod
    # def calcular_perimetro(self):
    #     raise NotImplementedError("Método abstrato deve ser implementado")


class Circulo(FormaGeometrica):
    def __init__(self,raio):
        self.raio = raio
    def calcular_area(self):
        return 3.14 * (self.raio ** 2)
    

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

circulo = Circulo(10)
print(circulo.calcular_area())


retangulo = Retangulo(10, 20)
print(retangulo.calcular_area())




class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
        self.ligado = False

    def ligar(self):
        print("Motor ligado")
        self.ligado = True
    

class Carro: 

    def __init__(self, marca, modelo, motor: Motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
    
    def exibir_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, potência: {self.motor.potencia}")
        self.buzinar()
    
    def buzinar(self):
        print("Buzinando...")


carro1 = Carro("Ford", "Mustang", Motor(potencia=300))
carro2 = Carro(marca= "Toyota", modelo= "Corolla", motor = Motor(potencia=200))

carro1.motor.ligar()
print(carro1.motor.ligado)
carro1.exibir_detalhes()
carro2.buzinar()

carro2.exibir_detalhes()
