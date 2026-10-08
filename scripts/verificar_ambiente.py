from pathlib import Path
import sys

try:
    import pandas as pd
    import numpy as np
    import faker
    print("Ambiente listo para iniciar Ciencia de Datos con Python")
    print("Python:", sys.version.split()[0])
    print("Pandas:", pd.__version__)
    print("NumPy:", np.__version__)
    print("Faker: instalado correctamente")
except ImportError as error:
    print("Falta instalar una librería:", error)

# Obtener la ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Carpetas obligatorias de la guía
carpetas = [
    "data/raw",
    "data/processed",
    "notebooks",
    "outputs",
    "docs",
    "scripts"
]

for carpeta in carpetas:
    ruta = BASE_DIR / carpeta
    ruta.mkdir(parents=True, exist_ok=True)
    print("Verificada:", ruta)