import funciones
print('Que desea hacer?')
print('Para sumar presione 1')
print('Para restar presione 2')
print('Para multiplicar presione 3')


try:
    a = int(input())
    

    if 0<=a<=3:
        num1= int(input('Digite un numero: '))
        num2= int(input('Digite un numero: '))
        if   a==1:
            print(funciones.suma(num1,num2))
        elif a==2:
            print(funciones.resta(num1,num2))
        elif a==3:
            print(funciones.producto(num1,num2))
    else:
        print('el usuario no ingreso lo solisitado')
    
except:
    print('el usuario no ingreso lo solisitado')
