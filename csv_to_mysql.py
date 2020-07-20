__author__ = "Wilebaldo Santana Hernández"
__copyright__ = "Copyright 2020, Peb2019"
__credits__ = ["Wilebaldo Santana Hernández"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Wilebaldo Santana Hernández"
__email__ = "wisahe@gmail.com"
__status__ = "Production"

# Importamos las librerías necesarias para el proyecto
# Pandas y SqlAlchemy
import pandas as pd
from sqlalchemy import create_engine

# Debido a que los datos del archivo CSV no tiene encabezados, creamos una lista
# con los nombres de todas las columnas.
columnas = [
    'id', 'codigo_entidad', 'entidad', 'nombre_escuela', 'cct', 'turno', 'municipio', 'localidad',
    'tipo_escuela', 'grado_evaluado', 'grado_marginacion', 'alumnos_programados',
    'lyc_alumnos_evaluados', 'mat_alumnos_evaluados',
    'lyc_porcentaje_evaluados', 'mat_porcentaje_evaluados',
    'lyc_representan_totalidad', 'mat_representan_totalidad',
    'escuela_parecidas', 'lyc_logro_alumnos_i',
    'lyc_logro_alumnos_ii', 'lyc_logro_alumnos_iii',
    'lyc_logro_alumnos_iv', 'lyc_logro_porcentajes_i',
    'lyc_logro_porcentajes_ii', 'lyc_logro_porcentajes_iii',
    'lyc_logro_porcentajes_iv', 'lyc_logro_escparecidas_i',
    'lyc_logro_escparecidas_ii', 'lyc_logro_escparecidas_iii',
    'lyc_logro_escparecidas_iv', 'mat_logro_alumnos_i',
    'mat_logro_alumnos_ii', 'mat_logro_alumnos_iii',
    'mat_logro_alumnos_iv', 'mat_logro_porcentajes_i',
    'mat_logro_porcentajes_ii', 'mat_logro_porcentajes_iii',
    'mat_logro_porcentajes_iv', 'mat_logro_escparecidas_i',
    'mat_logro_escparecidas_ii', 'mat_logro_escparecidas_iii', 'mat_logro_escparecidas_iv'
]

# Leemos el archivo CSV (Coma Separate Values) y le asignamos
# los nombres de las columnas
df = pd.read_csv('datos_csv/nac_escuelas_peb2019.csv', names=columnas)

# Creamos la conexión a la base de datos en MySQL
# En este caso, conectamos a la base de datos 'peb2019'
engine = create_engine('mysql+pymysql://root:w64xstvlmr.@localhost/peb2019')

# Escribimos el DataFrame a la tabla 'peb19' en la base de datos
df.to_sql('peb19', engine, index=False)