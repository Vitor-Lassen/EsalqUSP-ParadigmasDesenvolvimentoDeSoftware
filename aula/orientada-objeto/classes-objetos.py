class Carro: 

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def exibir_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")
        self.buzinar()
    
    def buzinar(self):
        print("Buzinando...")


carro1 = Carro("Ford", "Mustang", 1964)
carro2 = Carro(marca= "Toyota", modelo= "Corolla", ano=2020)

print(carro1.marca, carro1.modelo, carro1.ano)

carro1.exibir_detalhes()
carro2.buzinar()

carro2.exibir_detalhes()