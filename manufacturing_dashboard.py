#====================================================================
#Analisis de KPIs de manufactura
#KPIs 
# - Yield
# - Scrap Rate
# - Downtime
# - Produccion total
# - Produccion por maquina
#====================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#====================================================================
# 
# CARGA DE DATOS
#====================================================================

print("Cargando datos.....")

df = pd.read_csv(
    "production_data.csv"
)

print(df.head())

#====================================================================
# LIMPIEZA DE DATOS
#====================================================================

print("\nLimpiando datos....")
df.dropna(inplace = True)

#====================================================================
# KPI PRODUCCION TOTAL
#====================================================================

total_production = (
    df["Units_Produced"]
    .sum()
)

print("\nProduccion Total:")
print(total_production)

#====================================================================
# KPI DEFECTOS TOTALES
#====================================================================

total_defects = (
    df["Defects"]
    .sum()
)

print("\nDefectos Totales:")
print(total_defects)

#====================================================================
# KPI SCRAP RATE
#====================================================================

scrap_rate = (
    total_defects / 
    total_production
) * 100

print("\nScrap Rate (%):")
print(round(scrap_rate , 2))

#====================================================================
# KPI YIELD PROMEDIO
#====================================================================

avg_yield = (
    df["Yield"]
    .mean()
)

print("\nYield Promedio:")
print(round(avg_yield, 2))

#====================================================================
# KPI DOWUNTIME TOTAL
#====================================================================

downtime_total =  (
    df["Downtime_Min"]
    .sum()
)

print("\nDowntime Total (min): ")
print(downtime_total)

#====================================================================
# PRODUCCION POR MAQUINA
#====================================================================

production_machine = (
    df.groupby("Machine")
    ["Units_Produced"]
    .sum()
)

plt.figure(figsize = (8,5))

production_machine.plot(
      kind = "bar"
)         

plt.title(
    "Produccion por maquina"
)

plt.ylabel(
    "Unidades"
)

plt.tight_layout()

plt.show()


#====================================================================
# DEFECTOS POR MAQUINA
#====================================================================

machine_defects = (
    df.groupby("Machine")
    ["Defects"]
    .sum()
)

plt.figure(figsize=(8,5))

machine_defects.plot(
    kind = "bar"
)

plt.title(
    "Defectos por maquina"
)

plt.ylabel(
    "Cantidad de Defectos"
)

plt.tight_layout()

plt.show()


#====================================================================
# DOWNTIME POR MAQUINA
#====================================================================

downtime_machine = (
    df.groupby("Machine")
    ["Downtime_Min"]
    .sum()
)

plt.figure(figsize=(8,5))

downtime_machine.plot(
    kind = "bar"
)

plt.title(
    "Downtime por Maquina"
)

plt.ylabel(
    "Minutos"
)

plt.tight_layout()

plt.show()


#====================================================================
# HEATMAP DE CORRELACIÓN
#====================================================================

plt.figure(figsize=(8,5))

sns.heatmap(
    df[
        [
            "Units_Produced",
            "Defects",
            "Downtime_Min",
            "Yield"
        ]
    ].corr(),
    annot = True
)

plt.title(
    "Correlacion de Variables"
)

plt.show()


#====================================================================
# CONCLUSIONES AUTOMATICAS
#====================================================================

worst_machine = (
    machine_defects.idmax()
)

print("\n======================")
print("INSIGHTS")
print("========================")

print(
    f"La maquina con mas defectos es:  {worst_machine}"
)

print(
    f"Yield promedio: {avg_yield: .2f}%"
)

print(
    f"Scrap Rate: {scrap_rate: .2f}%"
)

print(
    f"Downtime Total: {downtime_total}"
)

