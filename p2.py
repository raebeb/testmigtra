#1. El promedio de tiempo de espera en zonas A y B
#2. El porcentaje de ciclos de faena que incluyeron alguna área de trabajo tipo 2
#3. Proponer otro análisis de los datos. Se valorará la creatividad y complejidad del análisis.
import json
import time
from datetime import datetime
from datetime import time
with open('data2.json') as f:
  data = json.load(f)

data_string = json.dumps(data)

decoded = json.loads(data_string)

cont = 0

for i in decoded:
  if (i["zone"] == "AE1" or i["zone"] == "AE2" or i["zone"] == "BE1" or i["zone"] == "BE2"):
    if (cont == 0):
      decodedTimein = datetime.fromisoformat(i["dt_in"])
      decodedTimeOut = datetime.fromisoformat(i["dt_out"])

      sum = decodedTimeOut - decodedTimein
      cont += 1
    
    decodedTimein = datetime.fromisoformat(i["dt_in"])
    decodedTimeOut = datetime.fromisoformat(i["dt_out"])

    totalTime = decodedTimeOut - decodedTimein
    sum = sum + totalTime
    cont += 1

print("El promedio de tiempo de espera en las areas AE1, AE2, BE1 y BE2 es: ", sum/cont)
############################################################################################
contW = 0
total = 0
for i in decoded:
  if(i["zone"] == "AW2" or i["zone"] == "BW2"):
    contW += 1
    total += 1
  else:
    total += 1
porc = (contW * 100) / total

print("El porcentaje de ciclos de faena que incluyeron un area de trabajo de tipo dos es: %.2f"% porc, "%")

####################################################################################
# que dia del mes se produjeron los mayores y menores tiempos de espera, en que estacion y a que camion corresponde

cont = 0
for i in decoded:
  if (i["zone"] == "AE1" or i["zone"] == "AE2" or i["zone"] == "BE1" or i["zone"] == "BE2"):
    decodedTimein = datetime.fromisoformat(i["dt_in"])
    decodedTimeOut = datetime.fromisoformat(i["dt_out"])
    totalTime = decodedTimeOut - decodedTimein
    
    if(cont == 0):
      tMenor = totalTime
      tMayor = totalTime
      currentDateMayor = decodedTimein.strftime("%m/%d/%y")
      truckNameMayor = i["asset"]
      zoneMayor = i["zone"]
      currentDateMenor = decodedTimein.strftime("%m/%d/%y")
      truckNameMenor = i["asset"]
      zoneMenor = i["zone"]
      cont += 1

    elif (totalTime > tMayor):
      tMayor = totalTime
      currentDateMayor = decodedTimein.strftime("%m/%d/%y")
      truckNameMayor = i["asset"]
      zoneMayor = i["zone"]
      cont += 1

    elif (totalTime < tMenor):
      tMenor = totalTime
      currentDateMenor = decodedTimein.strftime("%m/%d/%y")
      truckNameMenor = i["asset"]
      zoneMenor = i["zone"]
      cont += 1

print ("El mayor tiempo de espera fue de ", tMayor, " y se produjo el dia: ", currentDateMayor, "correspondiente al camion: ", truckNameMayor, "en la zona : ", zoneMayor)
print ("El menor tiempo de espera fue de: ", tMenor, " y se produjo el dia: ", currentDateMenor, "correspondiente al camion: ", truckNameMenor, "en la zona: ", zoneMenor)

#En que zona se produce el mayor tiempo de espera
cAE1 = 0
cAE2 = 0
cBE1 = 0
cBE2 = 0
zoneTime = []
cont = 0
for i in decoded:
  if (i["zone"] == "AE1"):
    decodedTimein = datetime.fromisoformat(i["dt_in"])
    decodedTimeOut = datetime.fromisoformat(i["dt_out"])
    totalTime = decodedTimeOut - decodedTimein
    if (cAE1 == 0):
      tAE1 = totalTime
      cAE1+=1
    else:
      tAE1 = tAE1 + totalTime
  
  if (i["zone"] == "AE2"):
    decodedTimein = datetime.fromisoformat(i["dt_in"])
    decodedTimeOut = datetime.fromisoformat(i["dt_out"])
    totalTime = decodedTimeOut - decodedTimein
    if (cAE2 == 0):
      tAE2 = totalTime
      cAE2+=1
    else:
      tAE2 = tAE2 + totalTime

  if (i["zone"] == "BE1"):
    decodedTimein = datetime.fromisoformat(i["dt_in"])
    decodedTimeOut = datetime.fromisoformat(i["dt_out"])
    totalTime = decodedTimeOut - decodedTimein
    if (cBE1 == 0):
      tBE1 = totalTime
      cBE1+=1
    else:
      tBE1 = tBE1 + totalTime

  if (i["zone"] == "BE2"):
    decodedTimein = datetime.fromisoformat(i["dt_in"])
    decodedTimeOut = datetime.fromisoformat(i["dt_out"])
    totalTime = decodedTimeOut - decodedTimein
    if (cBE2 == 0):
      tBE2 = totalTime
      cBE2+=1
    else:
      tBE2 = tBE2 + totalTime

zoneTime.append(tAE1)
zoneTime.append(tAE2)
zoneTime.append(tBE1)
zoneTime.append(tBE2)

mayor = zoneTime[0]
pos = 0
for i in range(0,3):
  print (zoneTime[i])
  if (zoneTime[i] > mayor):
    mayor = zoneTime[i]
    pos = i

if (pos == 0):
  eMayor = 'AE1'

if (pos == 1):
  eMayor = 'AE2'

if (pos == 2):
  eMayor = 'BE1'

if (pos == 3):
  eMayor = 'BE2'

print("Durante el periodo el mayor tiempo de espera se produjo en la estacion",eMayor, "con un tiempo total de:",mayor)