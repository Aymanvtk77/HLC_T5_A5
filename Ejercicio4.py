class CuentaBancaria:
    def __init__(self, saldo_inicio):
        self.__saldo = saldo_inicio

    def ver_el_saldo(self):
        return self.__saldo
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            print("El monton depositidao es mayor")

    def retirar(self, monto):
        if monto > 0:
            if monto <= self.__saldo:
                self.__saldo -= monto
            else:
                print("Fondos insuficientes")
        else:
            print("El monton a retirar debe ser positivo.")

cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(300)
print(cuenta.ver_el_saldo())