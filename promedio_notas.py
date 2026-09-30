#for numero in range (1, 60):
 #   print ("Turno")
  #  print (numero)
#print ("fin")
NotaTotal=0
rango=0
for i in range (1, 4):
    nota=float(input(f"Ingrese la nota {i}: "))
    NotaTotal+=nota
    rango+=i
print("fin del ciclo")
promedio= NotaTotal/rango
print(f"El promedio es: {promedio}")