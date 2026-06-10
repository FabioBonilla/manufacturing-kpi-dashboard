#Generador de datos de produccion 

#Se crea un dataset ficticio de manufactura para realizar el analisis de los KPIs

import pandas as pd
import numpy as np


#seed para lo resulltados autoreproducibles
np.random.seed(42)

#Cantidad de registros
rows = 5000

#creacion de datos simulados
data = {
    "Date" : pd.date_range(
        start = "2025-05-01",
        periods = rows,
        freq = "h"
    ),
    
    "Machine" :
        np.random.choice(
            ["M01" , "M02", "M03", "M04"],
            rows
    ),
    "Shift":np.random.choice(
        ["Day", "Night"],
        rows
    ),
    "Units_Produced" :
        np.random.randint(
            50,
            200,
            rows
    ),
    "Defects" :
        np.random.randint(
            0,
            10,
            rows
    ),
    "Downtime_Min" :
        np.random.randint(
            0,
            60,
            rows
    )            
        
}


df = pd.DataFrame(data)

#Calculo del Yield

df["Yield"] = (
    (df["Units_Produced"] - df["Defects"])
    / df["Units_Produced"]
) * 100


#Guardar CSV
df.to_csv(
    "production_data.csv",
    index = False
)

print("Archivo produccion_data.csv creado.")