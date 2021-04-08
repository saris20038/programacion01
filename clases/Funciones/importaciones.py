import Operaciones_string as Ops 
import Operacionesmatematicas as opm 

Ops.lineDesignEntrada1(70)
Valor1= int (input("ingrese el primer numero: "))
Valor2 = int (input("Ingrese el segundo numero: "))
mensaje_operacion =('Si {} los dos numeros da : ')
print(mensaje_operacion.format("resto"))
opm.calculadora(opm.sumar, Valor1, Valor2)
Ops.lineDesignEntrada1(70)
