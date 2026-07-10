import random, csv
from datetime import datetime

def leer_sensor(base=75, ruido=5):
    return round(base + random.uniform(-ruido, ruido),2)

lecturas = []
for i in range(100):
    temp = leer_sensor()
    estado = "¡ALERTA!" if temp > 85 or temp < 65 else "OK"
    lecturas.append({"id": i+1, "temp": temp, "estado": estado})

# Guardar CSV
with open("report_sesnor.csv", "w", newline="")as f:
    writer = csv.DictWriter(f, fieldnames=["id","temp","estado" ])
    writer.writeheader()
    writer.writerows(lecturas)

print(f"Promedio: {sum(r['temp'] for r in lecturas): .2f}°C")
print(f"Alertas: {sum(1 for r in lecturas if r['estado']=='¡ALERTA!')}")