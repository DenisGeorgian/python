# suma parametri nedefiniti
def suma_parametrii(*args, **kwargs):
    suma = 0
    for x in args:
        if isinstance(x,(int, float)):
            suma += x
    return suma

print(suma_parametrii(1, 5, -3, 'abc', [12, 56, 'cad']))

# recursivitate

def rec(lista):
   if not lista:
       return 0
   return lista[0] + rec(lista[1:])

lista_numere= [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_pare = []
lista_impare = []
for x in lista_numere:
 if x % 2 == 0:
    lista_pare.append(x)
 else:
    lista_impare.append(x)

print("Suma tuturor numerelor este: " + str(rec(lista_numere)))
print("Suma numerelor pare este: " + str(rec(lista_pare)))
print("Suma numerelor impare este: " + str(rec(lista_impare)))


#exceptii
def check_int(val_in):
    try:
        valoare = int(val_in)
        return valoare
    except ValueError:
        print("Eroare! Introdu un numar intreg la tastatura")
        return 0

val_in = input("Introdu valoarea: ")
val = check_int(val_in)
print(val)
