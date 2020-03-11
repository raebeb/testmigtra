#Determinar para la estructura de 3 niveles: Región - Provincia - Ciudad
#Extraer el promedio de la variable var1
#Extraer la suma de la variable var2 para la provincia 2
#Extraer el máximo de la variable var1 de la región 4

import json
def open_json():
  with open('data1.json') as f:
    data = json.load(f)

  data_string = json.dumps(data)
  decoded = json.loads(data_string)
  f.close()
  return decoded

def prom_var1():
  i = 0
  j = 0
  k = 0
  sum = 0
  decoded = open_json()
  for i in range(4):
    for j in range(2):
      for k in range(4):
        sum = sum + int(decoded[i]["children"][j]["children"][k]["values"]["var1"])

  print('Promedio var1: {}'.format(sum/32))

def suma_var2():
  sum = 0
  decoded = open_json()
  for i in range(4):
    sum = sum + int(decoded[0]["children"][1]["children"][i]["values"]["var2"]) 
  print("suma var2 provincia 2: {}".format(sum))

def max_var1():
  max = 0
  j = 0
  k = 0
  decoded = open_json()
  for j in range(2):
    for k in range(4):
      if(int(decoded[1]["children"][j]["children"][k]["values"]["var1"]) > max):
        max = int(decoded[3]["children"][j]["children"][k]["values"]["var1"])
  print("El maximo de var1 en la region 4 es: {}".format(max))
  
if __name__ == '__main__':
  prom_var1()
  suma_var2()
  max_var1()