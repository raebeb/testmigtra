#Determinar para la estructura de 3 niveles: Región - Provincia - Ciudad
#Extraer el promedio de la variable var1
#Extraer la suma de la variable var2 para la provincia 2
#Extraer el máximo de la variable var1 de la región 4

import json

with open('data1.json') as f:
  data = json.load(f)

data_string = json.dumps(data)

decoded = json.loads(data_string)

#print "Tenemos "+str(decoded["Fruteria"][1]["Verdura"][0]["Cantidad"])+" Lechugas."

#promedioVar1 = int(decoded[0]["children"][0]["children"][0]["values"]["var1"])

#prom = str(decoded[3]) --> Region

#prom = str(decoded[0]["children"][2]) --> prov

#prom = str(decoded[0]["children"][0]["children"][0]) --> ciuedad

i = 0
j = 0
k = 0
sum = 0
for i in range(4):
  for j in range(2):
    for k in range(4):
      sum = sum + int(decoded[i]["children"][j]["children"][k]["values"]["var1"])

print("Promedio var1: ", sum/32)

sum = 0
for i in range(4):
  sum = sum + int(decoded[0]["children"][1]["children"][i]["values"]["var2"]) 
print("suma var2 provincia 2: ", sum)


max = 0
j = 0
k = 0
for j in range(2):
  for k in range(4):
    if(int(decoded[1]["children"][j]["children"][k]["values"]["var1"]) > max):
      max = int(decoded[3]["children"][j]["children"][k]["values"]["var1"])
print("El maximo de var1 en la region 4 es: ", max)
  