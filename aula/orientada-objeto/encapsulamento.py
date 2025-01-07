class ContaBancaria:
    def __init__ (self, titular, saldo =0):
        self.titular = titular
        # __ defini  modificador do atributo como privado
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if (valor < 0 ):
            print("Valor inválido")
            return
        self.__saldo += valor
    
    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente")
        else:
            self.__saldo -= valor


conta_a = ContaBancaria("João", 1000)
conta_b = ContaBancaria(titular="Maria", saldo=2000)

conta_a.depositar(50_000_000)
conta_a.depositar(-500)
conta_a.sacar(200)
print(conta_a.get_saldo())
conta_a.sacar(2000)