# Asignacion de variable
nombre = input()
edad = int(input())
estatura = float(input())
toma_alcohol = "false"
print(f"Hola {nombre}, tu edad es {edad} y tu estatura es {estatura} cm, tomas alcohol? {toma_alcohol}")

# Limite de los enteros y flotantes en python: 
# Los enteros (int) tienen precisión ilimitada. 
# Los flotantes (float) a diferencia de los enteros (int) tienen unos valores mínimo y máximos que pueden representar. 
# La mínima precisión es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308 

# Suma de los primeros numeros pares
print("Ingrese el numero inicial")
n = int(input())
print("Ingrese el numero final")
nf = int(input())
suma = 0
print("**Estos son los primeros numeros pares**")
while n <= nf:
    if n % 2 == 0:
        print(n, end=" ")
        suma = suma + n
    n+=1
print("la suma de los numeros es: ",suma)
